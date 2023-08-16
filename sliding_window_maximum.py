import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_nums = [0] * (len(nums) - k + 1)

        max_nums[0] = max(nums[:k])

        j = 1

        for i in range(k, len(nums)):
            if nums[i] >= max_nums[j - 1]:
                max_nums[j] = nums[i]
            elif nums[i - k] != max_nums[j - 1]:
                max_nums[j] = max_nums[j - 1]
            else:
                max_nums[j] = max(nums[i - k + 1 : i + 1])

            j += 1

        return max_nums
