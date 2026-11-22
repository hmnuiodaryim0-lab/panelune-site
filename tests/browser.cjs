const { chromium } = require('playwright');
const { AxeBuilder } = require('@axe-core/playwright');
const fs = require('node:fs');
const path = require('node:path');
const output = process.env.QA_OUTPUT || '/tmp/panelune-site-qa';
fs.mkdirSync(output, { recursive: true });
(async()=>{
 const browser = await chromium.launch({headless:true,channel:'chrome'});
 const context=await browser.newContext(); const page=await context.newPage();
 const base=process.env.SITE_URL || 'http://127.0.0.1:8765/panelune-site/';const errors=[];const results=[];
 page.on('pageerror',e=>errors.push(e.message));
 page.on('response',r=>{if(r.status()>=400) errors.push(`${r.status()} ${r.url()}`)});
 for(const width of [320,375,390,768,1024,1440]){
  await page.setViewportSize({width,height:900});
  for(const lang of ['en','zh-Hans','zh-Hant','ja','ko']){
   await page.goto(base+(lang==='en'?'':lang+'/')); console.log('layout',width,lang);
   for(const img of await page.locator('img').all()) { await img.scrollIntoViewIfNeeded(); await img.evaluate(i=>i.decode()); }
   await page.evaluate(()=>Promise.all([...document.images].map(i=>i.decode().catch(()=>{}))));
   const data=await page.evaluate(()=>({lang:document.documentElement.lang,overflow:document.documentElement.scrollWidth>innerWidth,images:[...document.images].every(i=>i.complete&&i.naturalWidth>0),h1:document.querySelector('h1').innerText,links:[...document.querySelectorAll('a[href]')].map(a=>a.href)}));
   if(data.overflow||!data.images||data.lang!==lang)errors.push(JSON.stringify({width,lang,...data}));
   results.push({width,lang,overflow:data.overflow,images:data.images});
   if(width===390||width===1440){await page.evaluate(()=>scrollTo({top:0,behavior:'instant'}));await page.screenshot({path:path.join(output,`${lang}-${width}.png`),fullPage:true});}
  }
 }
 await page.setViewportSize({width:390,height:844}); await page.goto(base);
 for(const lang of ['zh-Hans','zh-Hant','ja','ko','en']){
  // Programmatic click keeps the page at the feature section, testing position preservation.
  await page.locator('#features').scrollIntoViewIfNeeded();
  const before=await page.locator('#features').evaluate(e=>e.getBoundingClientRect().top);
  await page.locator(`a[data-language="${lang}"]`).evaluate(e=>e.click());
  await page.waitForFunction(l=>document.documentElement.lang===l,lang);
  const after=await page.locator('#features').evaluate(e=>e.getBoundingClientRect().top);
  if(Math.abs(after-before)>2)errors.push(`scroll changed ${lang}: ${before}->${after}`);
  const canonical=await page.locator('link[rel=canonical]').getAttribute('href');
  if(!canonical.endsWith(lang==='en'?'/panelune-site/':`/${lang}/`))errors.push('stale canonical '+canonical);
  if(await page.locator('a[href$="privacy.html"]').first().getAttribute('href')!== (lang==='en'?'':'../')+'privacy.html')errors.push('privacy href');
 }
 // Reading further after a language switch must survive Back then Forward.
 await page.locator('#pro').scrollIntoViewIfNeeded();
 const historyBefore=await page.locator('#pro').evaluate(e=>e.getBoundingClientRect().top);
 await page.goBack(); await page.waitForFunction(()=>document.documentElement.lang==='ko');
 await page.goForward(); await page.waitForFunction(()=>document.documentElement.lang==='en');
 const historyAfter=await page.locator('#pro').evaluate(e=>e.getBoundingClientRect().top);
 if(Math.abs(historyAfter-historyBefore)>2)errors.push(`History position changed ${historyBefore}->${historyAfter}`);
 // Native fragment history must remain native.
 await page.goto(base); await page.locator('a[href=\"#features\"]').first().click();
 await page.waitForFunction(()=>Math.abs(document.querySelector('#features').getBoundingClientRect().top)<2);
 await page.goBack(); await page.waitForFunction(()=>scrollY<2);
 await page.goForward(); await page.waitForFunction(()=>Math.abs(document.querySelector('#features').getBoundingClientRect().top)<2);
 for(const target of ['','zh-Hans/','zh-Hant/','ja/','ko/','privacy.html','support.html','404.html']){
  await page.goto(base+target);
  const axe=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
  results.push({target,axe:axe.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>n.target)}))});
  if(axe.violations.some(v=>['serious','critical'].includes(v.impact))) errors.push(`Accessibility ${target}: ${JSON.stringify(results.at(-1))}`);
  const links=await page.locator('a').evaluateAll(nodes=>nodes.map(n=>n.href));
  for(const url of new Set(links.filter(x=>x.startsWith(base)))) {
   const parsed=new URL(url);const r=await context.request.get(parsed.href);if(r.status()!==200)errors.push(`Bad link ${url}`);
   if(parsed.hash){const html=await r.text();if(!html.includes(`id="${parsed.hash.slice(1)}"`))errors.push(`Bad anchor ${url}`);}
  }
 }
 const nojs=await browser.newContext({javaScriptEnabled:false});const p=await nojs.newPage();
 await p.goto(base);await p.locator('[data-language="ja"]').click();if(await p.locator('html').getAttribute('lang')!=='ja')errors.push('No-JS language links'); await nojs.close();
 fs.writeFileSync(path.join(output,'qa-results.json'),JSON.stringify({results,errors},null,2));
 console.log(JSON.stringify({layouts:30,errors,accessibility:results.filter(x=>x.axe)},null,2));
 await browser.close();if(errors.length)process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
