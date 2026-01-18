class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        """
        Calculate the vowel-to-consonant score of a given string.

        You are given a string `s` consisting of lowercase English letters,
        spaces, and digits. A vowel is defined as one of the characters:
        'a', 'e', 'i', 'o', or 'u'. Any other alphabetic character is
        considered a consonant.

        Let `v` be the number of vowels in `s` and `c` be the number of
        consonants in `s`. The score is defined as follows:
            - If c > 0, score = floor(v / c)
            - Otherwise, score = 0

        Args:
            s (str): Input string consisting of lowercase letters, spaces, and digits.

        Returns:
            int: The vowel-to-consonant score.

        Example:
            Input: s = "aio bcd"
            Output: 1

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        vowels = set("aeiou")
        v, c = 0, 0

        for ch in s:
            if ch.isalpha():
                if ch in vowels:
                    v += 1
                else:
                    c += 1

        return v // c if c > 0 else 0
