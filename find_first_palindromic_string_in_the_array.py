class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """Given a list of strings words, return the first palindromic string in the list. If there is no such string, return an empty string "".

        A string is palindromic if it reads the same forward and backward.

        Args:
            words (List[str]): The input list of strings to check for palindromes

        Returns:
            str: The first palindromic string found, or an empty string if none exists

        Example:
            >>> firstPalindrome(["abc", "car", "ada", "racecar", "cool"])
            'ada'

        Time complexity: O(n * m) - where n is the number of words and m is the length of the longest word
        Space complexity: O(1) - only using a single string variable

        LeetCode: Beats 100% of submissions
        """
        palindrome = ""

        for word in words:
            if word == word[::-1]:
                palindrome = word
                break

        return palindrome
