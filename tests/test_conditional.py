import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conditional import core


class ConditionalTest(unittest.TestCase):
    def test_no_headers(self):
        self.assertEqual(core.evaluate({}, '"x"', 0, core.Counter()), 200)

    def test_exact_match_304(self):
        self.assertEqual(core.evaluate({"if_none_match": '"x"'}, '"x"', 0, core.Counter()), 304)

    def test_no_match_200(self):
        self.assertEqual(core.evaluate({"if_none_match": '"y"'}, '"x"', 0, core.Counter()), 200)

    def test_if_match_missing_412(self):
        self.assertEqual(core.evaluate({"if_match": '"y"'}, '"x"', 0, core.Counter()), 412)

    def test_if_modified_since_304(self):
        self.assertEqual(core.evaluate({"if_modified_since": 100}, '"x"', 50, core.Counter()), 304)

    def test_counter_counts(self):
        counter = core.Counter()
        core.evaluate({"if_none_match": '"x"'}, '"x"', 0, counter)
        self.assertGreater(counter.scanned, 0)


if __name__ == "__main__":
    unittest.main()
