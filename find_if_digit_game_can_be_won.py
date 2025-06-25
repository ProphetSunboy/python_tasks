class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        """Determines if Alice can win the digit game.

        In this game, given a list of positive integers `nums`, Alice can choose
        either all single-digit numbers (1-9) or all double-digit numbers (10-99)
        from `nums`. The remaining numbers are given to Bob. Alice wins if the sum
        of her chosen numbers is strictly greater than the sum of Bob's numbers.

        Args:
            nums (list[int]): The input list of positive integers.

        Returns:
            bool: True if Alice can win the game, False otherwise.

        Example:
            >>> canAliceWin([2, 11, 10, 1, 3])
            True
            >>> canAliceWin([1, 2, 3, 4, 10])
            False

        LeetCode: Beats 100% of submissions
        """
        return sum([num for num in nums if num <= 9]) != sum(
            [num for num in nums if num > 9]
        )
