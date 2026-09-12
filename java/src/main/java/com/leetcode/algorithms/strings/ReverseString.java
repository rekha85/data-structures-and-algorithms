package com.leetcode.algorithms.strings;

import java.util.Scanner;

/** Provides an implementation for reversing the order of words in a string. */
public class ReverseString {

    /**
     * Reverses the order of words and removes extra whitespace between words.
     *
     * @param input the string whose words should be reversed
     * @return the words in reverse order separated by a single space, or an
     *         empty string for blank or {@code null} input
     */
    public static String reverseWords(String input) {
        if (input == null || input.isBlank()) {
            return "";
        }

        String[] words = input.strip().split("\\s+");
        StringBuilder reversed = new StringBuilder();

        for (int i = words.length - 1; i >= 0; i--) {
            if (reversed.length() > 0) {
                reversed.append(' ');
            }
            reversed.append(words[i]);
        }

        return reversed.toString();
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter a string to reverse:");
            String input = scanner.nextLine();
            System.out.println(reverseWords(input));
        }
    }
}
