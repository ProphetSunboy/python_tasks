class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Counts the number of unique palindromic subsequences of length three in
        a given string.

        Multiple ways to form the same subsequence are only counted once.

        Args:
            s (str): The input string consisting of lowercase English letters.

        Returns:
            int: The number of unique palindromic subsequences of length three.

        Example:
            Input: s = "aabca"
            Output: 3
                # The 3 unique palindromic subsequences are "aba", "aaa", and "aca".

        Time Complexity: O(26^2 * n), where n is the length of s (since we may check up to 26 different characters for each position).
        Space Complexity: O(1), as only constant extra space is used aside from the set of unique palindromes.
        """
        n = len(s)

        left_freq = [0] * 26
        right_freq = [0] * 26

        for char in s:
            right_freq[ord(char) - ord("a")] += 1

        unique_palindromes = set()

        for i in range(n):
            char = s[i]
            left_char_index = ord(char) - ord("a")

            right_freq[left_char_index] -= 1

            for middle_char_index in range(26):
                if (
                    left_freq[middle_char_index] > 0
                    and right_freq[middle_char_index] > 0
                ):
                    middle_char = chr(middle_char_index + ord("a"))
                    palindrome = char + middle_char + char
                    unique_palindromes.add(palindrome)

            left_freq[left_char_index] += 1

        return len(unique_palindromes)
