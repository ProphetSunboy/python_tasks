class Solution:
    def specialArray(self, nums: list[int]) -> int:
        """
        Return x if the list is special, otherwise, return -1. It can be proven
        that if nums is special, the value for x is unique.

        You are given an list nums of non-negative integers. nums is considered
        special if there exists a number x such that there are exactly x numbers
        in nums that are greater than or equal to x.

        Notice that x does not have to be an element in nums.

        :param list[int] nums: listof integer numbers
        :returns int x: number with exactly x numbers in nums that are greater
        than or equal to x

        Time complexity: O(nlogk)
        Space complexity: O(1)

        LeetCode: Beats 92.54%
        """
        l, r = 0, max(nums) + 1

        while l <= r:
            mid = l + (r - l) // 2

            counter = 0
            for num in nums:
                if num >= mid:
                    counter += 1

            if counter > mid:
                l = mid + 1
            elif counter < mid:
                r = mid - 1
            else:
                return mid

        return -1
