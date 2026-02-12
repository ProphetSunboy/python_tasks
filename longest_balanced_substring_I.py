class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Given a string s consisting of lowercase English letters,
        return the length of the longest balanced substring.

        A substring of s is called balanced if all distinct characters in the
        substring appear the same number of times.

        Args:
            s (str): The string to find the longest balanced substring of.

        Returns:
            int: The length of the longest balanced substring of s.

        Example:
            Input: s = "abbac"
            Output: 4

        Time Complexity: O(n^2), where n is the length of s.
        Space Complexity: O(1), as constant extra space is used.
        """
        longest_balanced = 0

        for i in range(len(s)):
            freqs = defaultdict(int)
            for j in range(i, len(s)):
                freqs[s[j]] += 1

                if len(set(freqs.values())) == 1:
                    if j - i + 1 > longest_balanced:
                        longest_balanced = j - i + 1

        return longest_balanced
