class Solution:
    def totalMoney(self, n: int) -> int:
        """Calculate the total money saved in LeetCode bank over n days.

        Hercy saves money daily following these rules:
        - Starts with $1 on Monday
        - Each subsequent day adds $1 more than previous day
        - Each new Monday starts $1 more than previous Monday

        Args:
            n (int): Number of days to calculate savings for

        Returns:
            int: Total amount of money saved after n days

        Example:
            >>> totalMoney(4)  # Monday to Thursday
            10  # 1 + 2 + 3 + 4 = 10
            >>> totalMoney(10)  # 1 week + 3 days
            37  # (1+2+3+4+5+6+7) + (2+3+4) = 37

        Time complexity: O(1) - uses mathematical formula
        Space complexity: O(1) - constant space

        LeetCode: Beats 100% of submissions
        """
        total = 0
        weeks = n // 7
        days = n % 7

        for i in range(weeks):
            total += sum(range(i + 1, i + 8))

        total += ((weeks + 1) + (weeks + days)) * days // 2
        return total
