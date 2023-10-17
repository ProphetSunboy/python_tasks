class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        """
        Given an integer list nums and an integer k, modify the list in the
        following way:

            choose an index i and replace nums[i] with -nums[i].

        You should apply this process exactly k times. You may choose the same
        index i multiple times.

        Return the largest possible sum of the list after modifying it in this
        way.

        :param list[int] nums: integer list
        :param int k: integer number of negations
        :returns int maximized_sum: largest possible sum of the list after
        modifying it

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 97.76%
        """
        s_nums = sorted(nums)
        maximized_sum = 0
        i = 0

        while k > 0 and i < len(s_nums):
            if s_nums[i] < 0:
                s_nums[i] *= -1
                maximized_sum += s_nums[i]
                k -= 1
            else:
                if k % 2:
                    if i != 0 and s_nums[i] > s_nums[i - 1]:
                        s_nums[i - 1] *= -1
                        maximized_sum += s_nums[i - 1] * 2 + s_nums[i]
                    else:
                        s_nums[i] *= -1
                        maximized_sum += s_nums[i]

                    k = 0
                else:
                    maximized_sum += s_nums[i]
                    k = 0

            i += 1

        if k > 0:
            i -= 1
            if k % 2:
                if i != 0 and s_nums[i] > s_nums[i - 1]:
                    s_nums[i - 1] *= -1
                    maximized_sum += s_nums[i - 1] * 2
                else:
                    s_nums[i] *= -1
                    maximized_sum += s_nums[i] * 2
            else:
                maximized_sum += s_nums[i]

            i += 1

        for j in range(i, len(s_nums)):
            maximized_sum += s_nums[j]

        return maximized_sum
