import sys
import unittest
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from leetcode.algorithms.strings.reversestring import reverse_string


class TestReverseString(unittest.TestCase):
    def test_reverses_words(self):
        self.assertEqual(reverse_string("the sky is blue"), "blue is sky the")

    def test_removes_extra_whitespace(self):
        self.assertEqual(
            reverse_string("  the   sky is blue  "),
            "blue is sky the",
        )

    def test_handles_tabs_between_words(self):
        self.assertEqual(reverse_string("hello\tworld"), "world hello")

    def test_handles_single_word(self):
        self.assertEqual(reverse_string("hello"), "hello")

    def test_handles_blank_input(self):
        self.assertEqual(reverse_string("   "), "")


if __name__ == "__main__":
    unittest.main()
