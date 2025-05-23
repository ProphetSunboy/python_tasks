class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """
        Given the list nums, for each nums[i] find out how many numbers in the
        list are smaller than it. That is, for each nums[i] you have to count
        the number of valid j's such that j != i and nums[j] < nums[i].

        :param list[int] nums: integer list
        :returns list[int]: how many numbers in the list are smaller than it

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 100%
        """
        l = list(sorted(nums))
        d = {l[0]: 0}

        m = l[0]
        for i, num in enumerate(l):
            if num > m:
                d[num] = i
                m = num

        for i, num in enumerate(nums):
            l[i] = d[num]

        return l