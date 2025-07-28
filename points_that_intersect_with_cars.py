class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        """Given a 0-indexed 2D integer list nums, where each element nums[i] = [start_i, end_i]
        represents a car parked from start_i to end_i (inclusive) on a number line,
        return the number of distinct integer points covered by at least one car.

        Args:
            nums (list[list[int]]): List of intervals, each representing the start and end positions of a car.

        Returns:
            int: The number of integer points on the line that are covered by any car.

        Example:
            >>> numberOfPoints([[3,6],[1,5],[4,7]])
            7  # All the points from 1 to 7 intersect at least one car, therefore the answer would be 7

        Time complexity: O(n log n), due to sorting the intervals.
        Space complexity: O(n), for storing merged intervals.

        LeetCode: Beats 100% of submissions
        """
        nums.sort()
        res = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i][0] <= res[-1][1]:
                if nums[i][1] > res[-1][1]:
                    res[-1][1] = nums[i][1]
            else:
                res.append(nums[i])

        return sum([num[1] - num[0] + 1 for num in res])
