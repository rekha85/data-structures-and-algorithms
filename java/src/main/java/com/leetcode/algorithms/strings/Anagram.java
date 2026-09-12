package com.leetcode.algorithms.strings;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Utility methods for checking whether two strings are anagrams.
 *
 * <p>The comparison is case-sensitive and treats whitespace and punctuation
 * as regular characters.</p>
 */
public final class Anagram {

    private Anagram() {
        // Utility class; do not instantiate.
    }

    /**
     * Returns whether the two strings contain the same Unicode code points
     * with the same frequencies.
     *
     * @param first the first string
     * @param second the second string
     * @return {@code true} when the strings are anagrams; otherwise
     *         {@code false}
     */
    public static boolean isAnagram(String first, String second) {
        if (first == null || second == null || first.length() != second.length()) {
            return false;
        }

        Map<Integer, Integer> codePointCounts = new HashMap<>();

        first.codePoints().forEach(codePoint ->
                codePointCounts.merge(codePoint, 1, Integer::sum));

        second.codePoints().forEach(codePoint ->
                codePointCounts.computeIfPresent(codePoint, (key, count) ->
                        count == 1 ? null : count - 1));

        return codePointCounts.isEmpty();
    }

    /** Runs a small interactive example from the command line. */
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the first string: ");
            String first = scanner.nextLine();

            System.out.print("Enter the second string: ");
            String second = scanner.nextLine();

            System.out.println("Are anagrams: " + isAnagram(first, second));
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
