package com.leetcode.algorithms.strings;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PalindromeTest {

    private final Palindrome palindrome = new Palindrome();

    @Test
    void acceptsPalindromeWithSpacesPunctuationAndMixedCase() {
        assertTrue(palindrome.isPalindrome("A man, a plan, a canal: Panama"));
    }

    @Test
    void rejectsNonPalindromeText() {
        assertFalse(palindrome.isPalindrome("race a car"));
    }

    @Test
    void acceptsEmptyAndNonLetterInput() {
        assertTrue(palindrome.isPalindrome(""));
        assertTrue(palindrome.isPalindrome("   "));
        assertTrue(palindrome.isPalindrome("."));
    }

    @Test
    void rejectsNullInput() {
        assertFalse(palindrome.isPalindrome(null));
    }
}
