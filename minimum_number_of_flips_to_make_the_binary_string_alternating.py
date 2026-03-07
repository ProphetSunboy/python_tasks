class Solution:
    def minFlips(self, s: str) -> int:
        """
        Given a binary string s, you may perform the following two types of
        operations any number of times:

            1. Remove the first character of s and append it to the end of the
            string.
            2. Flip any character in s (change '0' to '1', or '1' to '0').

        Return the minimum number of type-2 operations required to make s
        alternating (i.e., no two adjacent characters are the same).

        An alternating string example: "010", "1010".
        A non-alternating string example: "0100".

        Args:
            s (str): Input binary string.

        Returns:
            int: Minimum number of flips (type-2 operations) needed to make the
            string alternating.

        Time Complexity: O(n), where n is the length of the string, since each
                character is processed a constant number of times.
        Space Complexity: O(1), as constant extra space is used.

        LeetCode: Beats 96.24% of submissions
        """
        n = len(s)
        diff1 = 0
        diff2 = 0

        for i in range(n):
            if s[i] != ("0" if i % 2 == 0 else "1"):
                diff1 += 1
            else:
                diff2 += 1

        res = min(diff1, diff2)

        if n % 2 == 0:
            return res

        for i in range(n):
            if s[i] != ("0" if i % 2 == 0 else "1"):
                diff1 -= 1
            else:
                diff2 -= 1

            if s[i] != ("0" if (i + n) % 2 == 0 else "1"):
                diff1 += 1
            else:
                diff2 += 1

            res = min(res, diff1, diff2)

        return res
