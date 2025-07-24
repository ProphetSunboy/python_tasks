class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """Returns the length of the longest substring between two equal characters
        in the given string `s`, excluding the two characters themselves.
        If no such substring exists (i.e., no character appears at least twice), returns -1.

        Args:
            s (str): The input string consisting of lowercase English letters.

        Returns:
            int: The length of the longest substring between two equal characters, or -1 if none exists.

        Example:
            >>> maxLengthBetweenEqualCharacters("abca")
            2
            # The substring between the two 'a's is "bc", which has length 2.

            >>> maxLengthBetweenEqualCharacters("cbzxy")
            -1
            # No character appears twice.

        Time complexity: O(n), where n is the length of the string.
        Space complexity: O(1) (since the alphabet size is constant).

        LeetCode: Beats 100% of submissions
        """
        seen = dict()
        largest = -1

        for i, ch in enumerate(s):
            if ch not in seen:
                seen[ch] = i
            else:
                curr = i - seen[ch] - 1

                if curr > largest:
                    largest = curr

        return largest
