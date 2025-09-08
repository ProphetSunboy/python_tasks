class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        """
        Counts the number of triplets (i, j, k) in the given list such that:
            - 0 <= i < j < k < len(nums)
            - nums[i], nums[j], and nums[k] are pairwise distinct.

        Args:
            nums (List[int]): A 0-indexed list of positive integers.

        Returns:
            int: The number of triplets where all elements are distinct.

        Example:
            >>> unequalTriplets([4, 4, 2, 4, 3])
            3

        Time Complexity: O(n^3), where n is the length of nums.
        Space Complexity: O(1)
        """
        triplets = 0

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == nums[j]:
                    continue

                for k in range(j + 1, len(nums)):
                    if nums[i] == nums[k] or nums[j] == nums[k]:
                        continue
                    else:
                        triplets += 1

        return triplets
