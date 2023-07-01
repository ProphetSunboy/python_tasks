# First method
# class Solution:
#     def findClosestNumber(self, nums: list[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]

#         sorted_nums = sorted(nums, key=abs)

#         closest = sorted_nums[0]

#         for i in range(1, len(sorted_nums)):
#             if abs(sorted_nums[i]) > abs(closest):
#                 break
#             elif sorted_nums[i] > closest:
#                 closest = sorted_nums[i]

#         return closest


# Second method (Faster)
class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        """
        Given an integer array nums of size n, return the number with the value
        closest to 0 in nums. If there are multiple answers, return the number
        with the largest value.
        """
        closest = nums[0]
        abs_closest = abs(closest)

        for num in nums:
            abs_num = abs(num)

            if abs_num < abs_closest:
                closest = num
                abs_closest = abs_num
            elif abs_num == abs_closest and num > closest:
                closest = num
                abs_closest = abs_num

        return closest