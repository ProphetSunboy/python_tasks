# First solution
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the largest perimeter of a triangle
        with a non-zero area, formed from three of these lengths.
        If it is impossible to form any triangle of a non-zero area, return 0.
        """
        sort_nums = sorted(nums)
        right = len(nums) - 1
        while True:
            left = right - 2
            triangle_exist = True
            if left < 0:
                return 0
            lengths = sort_nums[left : right + 1]
            sum_lengths = sum(lengths)

            for length in lengths:
                if length >= sum_lengths - length:
                    right -= 1
                    triangle_exist = False

            if triangle_exist:
                return sum_lengths


# Second solution
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Given an integer list nums, return the largest perimeter of a triangle with a non-zero area,
        formed from three of these lengths. If it is impossible to form any triangle of a non-zero area,
        return 0.

        Args:
            nums (List[int]): List of integers representing side lengths.

        Returns:
            int: The largest possible perimeter of a valid triangle, or 0 if no such triangle exists.

        Example:
            >>> largestPerimeter([2,1,2])
            5
            >>> largestPerimeter([1,2,1])
            0
            >>> largestPerimeter([3,2,3,4])
            10

        Time Complexity: O(n log n) - due to sorting the input list.
        Space Complexity: O(1) - sorting can be done in-place.

        LeetCode: Beats 99.20% of submissions
        """
        nums.sort(reverse=True)
        i = 0

        while i < len(nums) - 2:
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]

            i += 1

        return 0
