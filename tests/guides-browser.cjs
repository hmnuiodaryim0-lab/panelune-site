const { chromium } = require('playwright');
const { AxeBuilder } = require('@axe-core/playwright');
const fs = require('node:fs');
const output = process.env.QA_OUTPUT || '/tmp/panelune-seo-phase2/qa';
const base = process.env.SITE_URL || 'http://127.0.0.1:8766/panelune-site/';
(async () => {
 fs.mkdirSync(output, {recursive: true});
 const browser = await chromium.launch({headless:true, channel:'chrome'});
 const context = await browser.newContext({javaScriptEnabled:false});
 // axe uses browser timers. Run its injected audit code in a separate JS-enabled
 // context; all navigation/layout assertions below still use the no-JS page.
 const auditContext = await browser.newContext();
 const auditPage = await auditContext.newPage();
 const page = await context.newPage(); const errors = []; const results = [];
 page.on('pageerror', e=>errors.push(e.message));
 page.on('response', r=>{if(r.status() >= 400) errors.push(`${r.status()} ${r.url()}`)});
 for(const lang of ['en','zh-Hans','zh-Hant','ja','ko']) {
  for(const slug of ['import-books','organize-library']) {
   const route = (lang==='en'?'':lang+'/')+'guides/'+slug+'/';
   for(const width of [320,390,1440]) {
    await page.setViewportSize({width,height:900}); await page.goto(base+route);
    const overflow = await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
    if(overflow) errors.push(`Overflow ${route} ${width}`);
    if(await page.locator('html').getAttribute('lang')!==lang) errors.push(`lang ${route}`);
    if(await page.locator('h1').count()!==1) errors.push(`heading ${route}`);
    results.push({route,width,overflow});
    if(width===390) await page.screenshot({path:`${output}/${lang}-${slug}.png`, fullPage:true});
   }
   await auditPage.goto(base+route);
   console.log('audit',route);
   const axe = await new AxeBuilder({page:auditPage}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
   results.push({route,violations:axe.violations.map(v=>({id:v.id,impact:v.impact}))});
   if(axe.violations.length) errors.push(`axe ${route}: ${axe.violations.map(v=>v.id)}`);
   const target = lang==='ja'?'en':'ja';
   await page.locator(`.language-nav a[lang="${target}"]`).click();
   if(!page.url().endsWith(`/guides/${slug}/`)) errors.push(`Topic lost ${route}`);
   if(await page.locator('html').getAttribute('lang')!==target) errors.push(`No-JS switch ${route}`);
   await page.locator('.guide-toc a').last().click();
   if(!page.url().includes('#')) errors.push(`TOC ${route}`);
  }
 }
 await browser.close();
 fs.writeFileSync(`${output}/guides-results.json`,JSON.stringify({results,errors},null,2));
 console.log(JSON.stringify({layouts:30,guideAxeChecks:10,errors},null,2));
 if(errors.length)process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
