class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Determines if two strings can be made equal by performing at most one swap
        on exactly one of the strings.

        A string swap is defined as choosing two indices (possibly the same) in a string and swapping the characters at those indices.
        The function returns True if it is possible to make both strings equal by performing at most one such swap on either s1 or s2.
        Otherwise, it returns False.

        Args:
            s1 (str): The first string.
            s2 (str): The second string, of the same length as s1.

        Returns:
            bool: True if the strings can be made equal with at most one swap, False otherwise.

        Example:
            >>> areAlmostEqual("bank", "kanb")
            True
            >>> areAlmostEqual("attack", "defend")
            False

        Time Complexity: O(n), where n is the length of the strings.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        if Counter(s1) != Counter(s2):
            return False

        ch_unequal = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ch_unequal += 1

        return ch_unequal <= 2
