import sys
import unittest
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from leetcode.algorithms.strings.palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_with_spaces_and_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("race a car"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_only_non_alphanumeric_characters(self):
        self.assertTrue(is_palindrome(" .,;!"))

    def test_unicode_text(self):
        self.assertTrue(is_palindrome("été"))


if __name__ == "__main__":
    unittest.main()
