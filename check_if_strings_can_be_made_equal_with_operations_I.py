class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        """Determines if two strings s1 and s2 of length 4 can be made equal by
        repeatedly swapping characters at positions i and j (where j - i = 2) in either string.

        Args:
            s1 (str): The first string of length 4.
            s2 (str): The second string of length 4.

        Returns:
            bool: True if s1 can be transformed into s2 using the allowed operations, False otherwise.

        Example:
            >>> canBeEqual("abcd", "cdab")
            True

        Time complexity: O(1)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return set([s1[0], s1[2]]) == set([s2[0], s2[2]]) and set(
            [s1[1], s1[3]]
        ) == set([s2[1], s2[3]])
