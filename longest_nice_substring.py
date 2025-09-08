class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        """
        Finds the longest "nice" substring in the given string.

        A string is considered "nice" if, for every letter it contains, both its uppercase and lowercase forms are present.
        For example, "abABB" is nice because both 'A'/'a' and 'B'/'b' appear, but "abA" is not nice because 'b' appears without 'B'.

        Args:
            s (str): The input string.

        Returns:
            str: The longest nice substring. If there are multiple, returns the earliest one. Returns an empty string if none exist.

        Example:
            >>> longestNiceSubstring("YazaAay")
            'aAa'

        Time Complexity: O(n^3), where n is the length of s.
        Space Complexity: O(n)
        """
        longest = ""

        for i in range(len(s)):
            for j in range(len(s) - 1, i, -1):
                curr = s[i : j + 1]
                nice = True
                for k in range(len(curr)):
                    if curr[k].islower() and curr[k].upper() not in curr:
                        nice = False
                        break
                    elif curr[k].isupper() and curr[k].lower() not in curr:
                        nice = False
                        break

                if nice:
                    if len(curr) > len(longest):
                        longest = curr

        return longest
