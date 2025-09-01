class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """
        Returns the maximum length of a substring of s such that each character appears at most twice.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest valid substring.

        Example:
            >>> maximumLengthSubstring("bcbbbcba")
            4

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(k), where k is the number of unique characters in s.

        LeetCode: Beats 100% of submissions
        """
        subs = Counter()
        max_subs = 0
        i, j = 0, 0

        while j < len(s):
            subs[s[j]] += 1

            if subs[s[j]] == 3:
                while subs[s[i]] != subs[s[j]]:
                    subs[s[i]] -= 1
                    i += 1

                subs[s[i]] -= 1
                i += 1
            else:
                if j - i + 1 > max_subs:
                    max_subs = j - i + 1

            j += 1

        return max_subs
