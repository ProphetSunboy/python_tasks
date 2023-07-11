class Solution:
    def climbStairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways
        can you climb to the top?

        LeetCode: Beats 99.31%
        """
        x, m = 1, 0
        for _ in range(n-1):
            x, m = x + m, x
        return x + m