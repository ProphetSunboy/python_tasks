class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        """Plays a number game and returns the resulting list.

        You are given a 0-indexed integer list `nums` of even length. Alice and
        Bob play a game with an empty list `arr`. In each round:
        1. Alice removes the minimum element from `nums`.
        2. Bob removes the minimum element from the remaining `nums`.
        3. Bob appends his removed element to `arr`.
        4. Alice appends her removed element to `arr`.
        The game continues until `nums` is empty.

        Args:
            nums (list[int]): An integer list of even length.

        Returns:
            list[int]: The resulting list `arr`.

        Example:
            >>> numberGame([5, 4, 2, 3])
            [3, 2, 5, 4]
            >>> numberGame([2, 5])
            [5, 2]

        LeetCode: Beats 100% of submissions
        """
        decreasing_nums = sorted(nums, reverse=True)
        arr = []

        while decreasing_nums:
            num = decreasing_nums.pop()
            arr.append(decreasing_nums.pop())
            arr.append(num)

        return arr
