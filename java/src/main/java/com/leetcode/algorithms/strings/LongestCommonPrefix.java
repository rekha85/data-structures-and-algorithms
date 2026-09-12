package com.leetcode.algorithms.strings;

import java.util.Scanner;

public class LongestCommonPrefix {

    static String longestCommonPrefix(String[] strs) {

        if (strs == null || strs.length == 0) {
            return "";
        }

        String prefix = strs[0];

        for(int i = 1; i< strs.length; i++){
            String temp = strs[i];
            int j = 0;
            while(j < prefix.length()
                     && j < temp.length()
                     && prefix.charAt(j) ==  temp.charAt(j) ) {
                j++;
            }

            prefix = prefix.substring(0, j);

            if(prefix.isEmpty())
                return "";
        }
        return prefix;
    }

    public static void main(String[] args) {
        String[] strings = null;
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the number of strings: ");
            int count = scanner.nextInt();

            strings = new String[count];
            System.out.println("Enter the strings separated by spaces:");

            for (int i = 0; i < count; i++) {
                strings[i] = scanner.next();
            }
        }catch (Exception ex){
            ex.printStackTrace();
        }
        String res = longestCommonPrefix(strings);
        System.out.println("Prefix:"+ res);
    }
}
