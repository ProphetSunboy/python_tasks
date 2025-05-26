class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        Given a list nums. We define a running sum of a list as
        runningSum[i] = sum(nums[0]…nums[i]).

        Return the running sum of nums.

        :param list[int] nums: integer list
        :returns list[int]: running sum of nums

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 100%
        """
        run_s = [nums[0]]

        for i in range(1, len(nums)):
            run_s.append(run_s[-1] + nums[i])

        return run_s
