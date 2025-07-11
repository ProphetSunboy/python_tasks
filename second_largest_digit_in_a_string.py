class Solution:
    def secondHighest(self, s: str) -> int:
        """Finds the second largest numerical digit in an alphanumeric string.

        Given a string `s` consisting of lowercase English letters and digits,
        this function returns the second largest digit (as an integer) that
        appears in `s`. If there is no such digit, returns -1.

        Args:
            s (str): The input alphanumeric string.

        Returns:
            int: The second largest digit in `s`, or -1 if it does not exist.

        Example:
            >>> secondHighest("dfa12321afd")
            2
            >>> secondHighest("abc1111")
            -1

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(1), since the set of possible digits is constant.

        LeetCode: Beats 100% of submissions
        """
        digits = list()

        for ch in set(s):
            if ch.isdigit():
                digits.append(ch)

        digits.sort()

        return -1 if len(digits) < 2 else int(digits[-2])
