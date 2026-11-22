import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReleaseTests(unittest.TestCase):
    def test_release_generator_exists(self):
        self.assertTrue((ROOT / 'scripts/build.py').exists(), 'A single source must generate crawlable release-aware pages')

    def test_both_release_states(self):
        if not (ROOT / 'scripts/build.py').exists():
            self.skipTest('Generator not implemented yet')
        spec = importlib.util.spec_from_file_location('build', ROOT / 'scripts/build.py')
        build = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(build)
        for status in ('coming-soon', 'available'):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as tmp:
                build.build(Path(tmp), status=status)
                home = (Path(tmp) / 'index.html').read_text()
                schema = json.loads(home.split('<script type="application/ld+json">')[1].split('</script>')[0])
                self.assertEqual(schema['availableOnDevice'], ['iPhone', 'iPad'] if status == 'available' else ['iPad'])
                self.assertEqual(schema['softwareVersion'], '1.2.0' if status == 'available' else '1.1.1')
                self.assertNotIn('aggregateRating', schema)
                self.assertNotIn('offers', schema)
                self.assertIn('On iPhone and iPad.' if status == 'available' else 'iPhone support coming soon', home)
                support = (Path(tmp) / 'support.html').read_text()
                self.assertIn('available on iPhone and iPad' if status == 'available' else 'iPhone support is coming soon', support)
                for lang in ('en', 'zh-Hans', 'zh-Hant', 'ja', 'ko'):
                    page = Path(tmp) / ('index.html' if lang == 'en' else lang + '/index.html')
                    content = page.read_text()
                    self.assertIn(f'<html lang="{lang}">', content)
                    self.assertEqual(content.split('</head>')[0].count('hreflang='), 6)
                    self.assertEqual(content.count('<h1>'), 1)
                    self.assertNotIn('$2.99', content)
                    self.assertNotIn('Duo', content)
                    if status == 'available': self.assertNotIn('coming soon', content)
                    for other in ('zh-Hans', 'zh-Hant', 'ja', 'ko'):
                        self.assertIn(f'/panelune-site/{other}/', content)


class StaticSiteTests(unittest.TestCase):
    def test_generated_files_match_sources(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(['python3', str(ROOT / 'scripts/build.py'), '--output', tmp], check=True, capture_output=True)
            for path in Path(tmp).rglob('*'):
                if path.is_file():
                    self.assertEqual(path.read_bytes(), (ROOT / path.relative_to(tmp)).read_bytes(), str(path))

    def test_local_links_and_assets(self):
        from html.parser import HTMLParser
        from urllib.parse import urlparse, unquote
        class Page(HTMLParser):
            def __init__(self, text):
                super().__init__(); self.urls=[]; self.ids=set(); self.feed(text)
            def handle_starttag(self, tag, attrs):
                a=dict(attrs)
                if a.get('id'): self.ids.add(a['id'])
                for attr in ('href','src'):
                    if a.get(attr): self.urls.append(a[attr])
                if 'srcset' in a:
                    self.urls.extend(part.strip().split()[0] for part in a['srcset'].split(','))
                if tag=='img':
                    assert a.get('alt') and a.get('width') and a.get('height') and a.get('loading')=='lazy'
        files=[ROOT/'index.html',ROOT/'privacy.html',ROOT/'support.html',ROOT/'404.html']
        files += [ROOT/lang/'index.html' for lang in ('zh-Hans','zh-Hant','ja','ko')]
        for file in files:
            for link in Page(file.read_text()).urls:
                url=urlparse(link)
                if url.scheme or url.netloc: continue
                if url.path.startswith('/panelune-site/'):
                    target=ROOT/unquote(url.path.removeprefix('/panelune-site/'))
                else: target=file.parent/unquote(url.path) if url.path else file
                if target.is_dir(): target=target/'index.html'
                self.assertTrue(target.is_file(), f'{file}: {link}')
                if url.fragment:
                    self.assertIn(unquote(url.fragment), Page(target.read_text()).ids, link)

if __name__ == '__main__':
    unittest.main()
