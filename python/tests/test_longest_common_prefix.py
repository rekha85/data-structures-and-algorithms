import sys
import unittest
from pathlib import Path


# Add python/src to the import path when tests are run from the project root.
SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from leetcode.algorithms.strings.longest_common_prefix import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual(
            longest_common_prefix(["flower", "flow", "flight"]),
            "fl",
        )

    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_single_string(self):
        self.assertEqual(longest_common_prefix(["python"]), "python")

    def test_empty_string(self):
        self.assertEqual(longest_common_prefix(["", "test"]), "")


if __name__ == "__main__":
    unittest.main()
