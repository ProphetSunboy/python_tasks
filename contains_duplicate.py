class Solution:
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        """
        Given an integer array nums and an integer k, return True if there are
        two distinct indices i and j in the array such that nums[i] == nums[j]
        and abs(i - j) <= k.
        """
        seen = {}

        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = i
            else:
                if i - seen[num] > k:
                    seen[num] = i
                else:
                    return True

        return False