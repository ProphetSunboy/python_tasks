class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        You are given a positive integer num consisting only of digits 6 and 9.

        Return the maximum number you can get by changing at most one digit
        (6 becomes 9, and 9 becomes 6).


        LeetCode Beats 100%
        """
        max_num = num
        s = str(num)

        for i, n in enumerate(s):
            if n == "6":
                return int(s[:i] + "9" + s[i + 1 :])

        return max_num
