"""Robots directive parsing must not report a blocked page as indexable."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('live_check', Path(__file__).resolve().parents[1]/'scripts/check_live.py')
live_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(live_check)

class LiveSignalsTests(unittest.TestCase):
    def test_comma_separated_robots_directives_are_normalized(self):
        page = live_check.Signals('<meta name="robots" content="max-snippet:20, NONE"><meta name="googlebot" content=" noindex , follow ">')
        self.assertEqual(page.robots, ['max-snippet:20', 'none', 'noindex', 'follow'])

if __name__ == '__main__': unittest.main()
