package com.leetcode.algorithms.strings;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class AnagramTest {

    @Test
    void returnsTrueWhenStringsAreAnagrams() {
        assertTrue(Anagram.isAnagram("listen", "silent"));
    }

    @Test
    void returnsFalseWhenStringsAreNotAnagrams() {
        assertFalse(Anagram.isAnagram("hello", "world"));
    }

    @Test
    void respectsCharacterFrequency() {
        assertFalse(Anagram.isAnagram("aab", "abb"));
    }

    @Test
    void treatsCaseAndWhitespaceAsSignificant() {
        assertFalse(Anagram.isAnagram("Listen", "silent"));
        assertFalse(Anagram.isAnagram("the eyes", "they see"));
    }

    @Test
    void supportsUnicodeCodePoints() {
        assertTrue(Anagram.isAnagram("😀a", "a😀"));
    }

    @Test
    void returnsFalseForNullInput() {
        assertFalse(Anagram.isAnagram(null, "test"));
        assertFalse(Anagram.isAnagram("test", null));
    }
}
