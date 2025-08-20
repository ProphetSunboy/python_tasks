class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        """
        Counts the number of times an ant returns to the boundary after moving according to a sequence of steps.

        The ant starts at the boundary (position 0) and moves according to the values in the input list `nums`:
            - If nums[i] < 0, the ant moves left by -nums[i] units.
            - If nums[i] > 0, the ant moves right by nums[i] units.

        After each move, if the ant is exactly at the boundary (position 0), it is counted as a return to the boundary.
        Crossing the boundary during a move does not count; only landing exactly on the boundary after a move is considered.

        Args:
            nums (list[int]): A list of non-zero integers representing the ant's moves.

        Returns:
            int: The number of times the ant returns to the boundary (position 0) after a move.

        Example:
            >>> returnToBoundaryCount([2, 3, -5])
            1

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 95.16% of submissions
        """
        bound = 0
        curr = 0

        for num in nums:
            curr += num

            if curr == 0:
                bound += 1

        return bound
