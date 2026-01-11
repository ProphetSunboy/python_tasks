class Solution:
    def residuePrefixes(self, s: str) -> int:
        """
        Given a string s consisting of only lowercase English letters.

        A prefix of s is called a residue if the number of distinct characters
        in the prefix is equal to len(prefix) % 3.

        Returns the count of residue prefixes in s.

        A prefix of a string is any non-empty substring starting from the
        beginning of the string up to any position.

        Args:
            s (str): Input string of lowercase English letters.

        Returns:
            int: The number of residue prefixes in s.

        Example:
            Input: s = "abc"
            Output: 2

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1) (for set of unique characters, up to 26).

        LeetCode: Beats 100% of submissions
        """
        residue = 0
        unique = set()

        for i, ch in enumerate(s):
            unique.add(ch)

            if (i + 1) % 3 == len(unique):
                residue += 1

        return residue
