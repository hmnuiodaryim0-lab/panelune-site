#!/usr/bin/env python3
"""Read-only deployment check. HTTP success never proves search indexing."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Signals(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.canonicals=[]; self.robots=[]; self.feed(html)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='link' and a.get('rel')=='canonical': self.canonicals.append(a.get('href'))
        if tag=='meta' and a.get('name','').lower() in ('robots','googlebot','bingbot'):
            self.robots.extend(value.strip().lower() for value in a.get('content','').split(','))

def fetch(url, agent='Panelune-SEO-check/1.0'):
    # No cookies or authentication. curl separates response headers from the body.
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        headers=Path(tmp)/'headers'; body=Path(tmp)/'body'
        r=subprocess.run(['curl','-sS','-L','--max-time','30','--max-redirs','5','-A',agent,'-D',str(headers),'-o',str(body),'-w','%{http_code}\n%{url_effective}',url],capture_output=True,text=True)
        status,_,final=r.stdout.partition('\n')
        return dict(status=status,finalUrl=final,error=r.stderr.strip() if r.returncode else '',headers=headers.read_text() if headers.exists() else '',body=body.read_bytes() if body.exists() else b'')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True,help='JSON receipt path, preferably outside the published tree')
    args=parser.parse_args()
    config=json.loads((ROOT/'content/site.json').read_text()); base=config['baseUrl']
    urls=[n.text for n in ET.parse(ROOT/'sitemap.xml').findall('{*}url/{*}loc')]
    def check(url):
        r=fetch(url); relative=url.removeprefix(base); p=ROOT/(relative+'index.html' if url.endswith('/') else relative)
        html=r['body'].decode('utf-8',errors='replace'); signals=Signals(html)
        blocked=bool({'noindex', 'none'}.intersection(signals.robots)) or any('noindex' in line.lower() or 'none' in line.lower() for line in r['headers'].splitlines() if line.lower().startswith('x-robots-tag:'))
        return {'url':url,'status':r['status'],'finalUrl':r['finalUrl'],'canonical':signals.canonicals,'bytes':len(r['body']),'matchesLocal':r['body']==p.read_bytes(),'noindex':blocked,'error':r['error'],'ok':r['status']=='200' and r['finalUrl']==url and signals.canonicals==[url] and not blocked and r['body']==p.read_bytes()}
    with ThreadPoolExecutor(max_workers=4) as pool: pages=list(pool.map(check,urls))
    sitemap=fetch(base+'sitemap.xml')
    sitemap_ok=sitemap['status']=='200' and sitemap['body']==(ROOT/'sitemap.xml').read_bytes()
    origin=urlparse(base); robots=fetch(f'{origin.scheme}://{origin.netloc}/robots.txt')
    probes=[]
    for agent in ('Googlebot','bingbot'):
        r=fetch(base+'guides/import-books/',agent)
        probes.append({'agent':agent,'status':r['status'],'matchesLocal':r['body']==(ROOT/'guides/import-books/index.html').read_bytes(),'ok':r['status']=='200' and r['body']==(ROOT/'guides/import-books/index.html').read_bytes()})
    exclusions=[]
    for path in ('seo-missing-page-check','docs/seo/SEO-AUDIT.md','content/search-verification.json','scripts/build.py'):
        r=fetch(base+path)
        exclusions.append({'path':path,'status':r['status'],'ok':r['status']=='404'})
    receipts={'checkedAtUtc':datetime.now(timezone.utc).isoformat(),'baseUrl':base,'pages':pages,'sitemapMatchesLocal':sitemap_ok,'originRobots':{'url':f'{origin.scheme}://{origin.netloc}/robots.txt','status':robots['status'],'body':robots['body'].decode('utf-8',errors='replace') if robots['status']=='200' else None},'userAgentProbes':probes,'excludedPaths':exclusions,'indexingStatus':'Unknown: requires verified Google/Bing property data. User-agent probes are not real search-engine crawls.'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n')
    errors=[r for r in pages+probes+exclusions if not r['ok']]
    print(json.dumps({'pages':len(pages),'passedPages':sum(p['ok'] for p in pages),'sitemapMatchesLocal':sitemap_ok,'errors':errors,'receipt':str(args.output)},ensure_ascii=False,indent=2))
    raise SystemExit(bool(errors) or not sitemap_ok)

if __name__=='__main__': main()
