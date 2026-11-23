"""Contracts that break when nested guide routes or crawl signals regress."""
import importlib.util
import json
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://hmnuiodaryim0-lab.github.io/panelune-site/'
LANGS = ('en', 'zh-Hans', 'zh-Hant', 'ja', 'ko')
TOPICS = ('import-books', 'organize-library')
spec = importlib.util.spec_from_file_location('site_build', ROOT/'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []; self.anchors = []; self.meta = {}; self.h1 = 0
        self.lang = None; self.scripts = []; self.data = ''; self.in_schema = False
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'link': self.links.append(a)
        if tag == 'a': self.anchors.append(a.get('href', ''))
        if tag == 'h1': self.h1 += 1
        if tag == 'meta': self.meta[a.get('name', a.get('property'))] = a.get('content')
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_schema = True; self.data = ''
    def handle_data(self, data):
        if self.in_schema: self.data += data
    def handle_endtag(self, tag):
        if tag == 'script' and self.in_schema:
            self.scripts.append(json.loads(self.data)); self.in_schema = False

class SeoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        build.build(self.root)

    def test_sitemap_exactly_covers_public_canonical_pages(self):
        urls = [node.text for node in ET.parse(self.root/'sitemap.xml').findall('{*}url/{*}loc')]
        expected = {BASE+'privacy.html', BASE+'support.html'}
        for lang in LANGS:
            prefix = '' if lang == 'en' else lang+'/'
            expected.add(BASE+prefix)
            expected.update(BASE+prefix+'guides/'+t+'/' for t in TOPICS)
        self.assertEqual(set(urls), expected)
        self.assertEqual(len(urls), 17)
        for url in urls:
            path = url.removeprefix(BASE)
            html = (self.root/(path+'index.html' if url.endswith('/') else path)).read_text()
            p = Page(html)
            self.assertEqual([x['href'] for x in p.links if x.get('rel') == 'canonical'], [url])
            self.assertNotIn('noindex', p.meta.get('robots', ''))

    def test_guide_alternates_stay_on_same_topic_and_work_without_js(self):
        for topic in TOPICS:
            expected = {lang: BASE+('' if lang == 'en' else lang+'/')+'guides/'+topic+'/' for lang in LANGS}
            expected['x-default'] = BASE+'guides/'+topic+'/'
            for lang in LANGS:
                route = ('' if lang == 'en' else lang+'/')+'guides/'+topic+'/'
                path = self.root/route/'index.html'
                self.assertTrue(path.exists(), route)
                p = Page(path.read_text())
                self.assertEqual(p.lang, lang); self.assertEqual(p.h1, 1)
                self.assertTrue(p.meta.get('description'))
                self.assertEqual({x['hreflang']: x['href'] for x in p.links if x.get('rel')=='alternate'}, expected)
                links = {urljoin(BASE+route, href) for href in p.anchors}
                self.assertTrue(set(expected.values()).issubset(links))
                self.assertTrue(p.scripts)
                self.assertNotIn('FAQPage', path.read_text())

    def test_guides_reachable_from_each_homepage_and_cross_linked(self):
        for lang in LANGS:
            prefix = '' if lang == 'en' else lang+'/'
            home = Page((self.root/prefix/'index.html').read_text())
            home_links = {urljoin(BASE+prefix, h) for h in home.anchors}
            for topic in TOPICS:
                url = BASE+prefix+'guides/'+topic+'/'
                self.assertIn(url, home_links)
                path = self.root/prefix/'guides'/topic/'index.html'
                if not path.exists(): continue
                links = {urljoin(url, h) for h in Page(path.read_text()).anchors}
                self.assertIn(BASE+prefix, links)
                for other in TOPICS:
                    if other != topic: self.assertIn(BASE+prefix+'guides/'+other+'/', links)

    def test_verification_disabled_until_real_tokens_configured(self):
        original = build.read
        with patch.object(build, 'read', side_effect=lambda name: {'google':'', 'bing':''} if name=='search-verification' else original(name)):
            build.build(self.root)
        p = Page((self.root/'index.html').read_text())
        self.assertNotIn('google-site-verification', p.meta)
        self.assertNotIn('msvalidate.01', p.meta)
        def configured(name):
            if name == 'search-verification':
                return {'google': 'unit-test<&"token', 'bing': 'unit-test-bing'}
            return original(name)
        with patch.object(build, 'read', side_effect=configured):
            build.build(self.root)
        p = Page((self.root/'index.html').read_text())
        self.assertEqual(p.meta.get('google-site-verification'), 'unit-test<&"token')
        self.assertEqual(p.meta.get('msvalidate.01'), 'unit-test-bing')
        # Test values only in temporary output, never deployed content.

    def test_homepage_descriptions_follow_release_state(self):
        for status in ('coming-soon', 'available'):
            build.build(self.root, status=status)
            for lang in LANGS:
                with self.subTest(status=status, lang=lang):
                    p = Page((self.root/('' if lang == 'en' else lang)/'index.html').read_text())
                    descriptions = [p.meta[key] for key in ('description', 'og:description', 'twitter:description')]
                    descriptions.append(p.scripts[0]['description'])
                    self.assertTrue(all(text == descriptions[0] for text in descriptions))
                    for text in descriptions:
                        self.assertEqual('iPhone' in text, status == 'available')
                    if status == 'coming-soon':
                        self.assertEqual(descriptions[0], build.read(lang)['description'])

    def test_current_release_is_preserved(self):
        config = json.loads((ROOT/'content/site.json').read_text())
        self.assertEqual(config['iphoneReleaseStatus'], 'available')
        for lang in LANGS:
            p = Page((self.root/('' if lang=='en' else lang)/'index.html').read_text())
            self.assertEqual(p.scripts[0]['softwareVersion'], '1.2.0')
            self.assertEqual(p.scripts[0]['availableOnDevice'], ['iPhone', 'iPad'])

if __name__ == '__main__': unittest.main()
