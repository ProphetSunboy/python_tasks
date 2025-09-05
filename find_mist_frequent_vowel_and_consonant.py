class Solution:
    def maxFreqSum(self, s: str) -> int:
        """
        Given a string s consisting of lowercase English letters ('a' to 'z'), find:

        - The vowel (one of 'a', 'e', 'i', 'o', 'u') with the maximum frequency.
        - The consonant (all other letters) with the maximum frequency.

        Return the sum of these two frequencies.

        If there are multiple vowels or consonants with the same maximum frequency, any one may be chosen.
        If there are no vowels or no consonants in the string, treat their frequency as 0.

        Args:
            s (str): The input string.

        Returns:
            int: The sum of the maximum frequency of any vowel and any consonant in s.

        Example:
            >>> maxFreqSum("banana")
            5   # 'a' appears 3 times (vowel), 'n' appears 2 times (consonant), so 3 + 2 = 5

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        cons = {"b": 0}

        for ch in s:
            if ch in vowels:
                vowels[ch] = vowels.get(ch, 0) + 1
            else:
                cons[ch] = cons.get(ch, 0) + 1

        return max(vowels.values()) + max(cons.values())
