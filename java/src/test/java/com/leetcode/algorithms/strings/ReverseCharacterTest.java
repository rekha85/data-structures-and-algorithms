package com.leetcode.algorithms.strings;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ReverseCharacterTest {

    @Test
    void reversesLettersOnly() {
        assertEquals(
                "Qedo1ct-eeLg=ntse-T!",
                ReverseCharacter.reverseOnlyLetters("Test1ng-Leet=code-Q!")
        );
    }

    @Test
    void preservesDigitsAndSymbols() {
        assertEquals("dc-ba!", ReverseCharacter.reverseOnlyLetters("ab-cd!"));
    }

    @Test
    void handlesInputWithoutLetters() {
        assertEquals("123-!", ReverseCharacter.reverseOnlyLetters("123-!"));
    }

    @Test
    void handlesEmptyAndNullInput() {
        assertEquals("", ReverseCharacter.reverseOnlyLetters(""));
        assertEquals(null, ReverseCharacter.reverseOnlyLetters(null));
    }
}
