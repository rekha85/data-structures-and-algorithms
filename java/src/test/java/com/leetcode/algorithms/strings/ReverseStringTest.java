package com.leetcode.algorithms.strings;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ReverseStringTest {

    @Test
    void reversesWordsInNormalInput() {
        assertEquals("blue is sky the", ReverseString.reverseWords("the sky is blue"));
    }

    @Test
    void removesLeadingTrailingAndRepeatedWhitespace() {
        assertEquals("world hello", ReverseString.reverseWords("  hello   world  "));
    }

    @Test
    void handlesDifferentWhitespaceCharacters() {
        assertEquals("world hello", ReverseString.reverseWords("hello\tworld"));
    }

    @Test
    void handlesSingleWord() {
        assertEquals("hello", ReverseString.reverseWords("hello"));
    }

    @Test
    void returnsEmptyStringForBlankOrNullInput() {
        assertEquals("", ReverseString.reverseWords("   "));
        assertEquals("", ReverseString.reverseWords(null));
    }
}
