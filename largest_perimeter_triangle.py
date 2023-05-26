class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the largest perimeter of a triangle
        with a non-zero area, formed from three of these lengths.
        If it is impossible to form any triangle of a non-zero area, return 0.
        """
        sort_nums = sorted(nums)
        right = len(nums)-1
        while True:
            left = right - 2
            triangle_exist = True
            if left < 0:
                return 0
            lengths = sort_nums[left:right+1]
            sum_lengths = sum(lengths)
            
            for length in lengths:
                if length >= sum_lengths - length:
                    right -= 1
                    triangle_exist = False

            if triangle_exist:
                return sum_lengths