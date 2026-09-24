package com.leetcode.algorithms.strings;

import java.util.Scanner;

/** Reverses letters while keeping digits and symbols in their original positions. */
public final class ReverseCharacter {

    private ReverseCharacter() {
        // Utility class; do not instantiate.
    }

    /**
     * Reverses only the letters in the input string.
     *
     * <p>Non-letter characters remain at their original indexes.</p>
     *
     * @param input the string to process
     * @return the string with its letters reversed, or {@code null} when the
     *         input is {@code null}
     */
    public static String reverseOnlyLetters(String input) {
        if (input == null || input.length() < 2) {
            return input;
        }

        char[] characters = input.toCharArray();
        int left = 0;
        int right = characters.length - 1;

        while (left < right) {
            while (left < right && !Character.isLetter(characters[left])) {
                left++;
            }

            while (left < right && !Character.isLetter(characters[right])) {
                right--;
            }

            char temporary = characters[left];
            characters[left] = characters[right];
            characters[right] = temporary;

            left++;
            right--;
        }

        return new String(characters);
    }

    /** Runs the solution interactively from the command line. */
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter a string: ");
            String input = scanner.nextLine();
            System.out.println(reverseOnlyLetters(input));
        }
    }
}
