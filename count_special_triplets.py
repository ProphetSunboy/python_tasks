class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        """
        Counts the number of special triplets in the given integer list nums.

        A special triplet is defined as a triplet of indices (i, j, k) such that:
            - 0 <= i < j < k < n, where n = len(nums)
            - nums[i] == nums[j] * 2
            - nums[k] == nums[j] * 2

        Returns the total number of such triplets modulo 10^9 + 7.

        Args:
            nums (List[int]): A list of positive integers.

        Returns:
            int: The total number of special triplets in the list.

        Example:
            Input: nums = [8, 4, 8, 2]
            Special triplets:
            - (0, 1, 2): nums[0]=8, nums[1]=4, nums[2]=8
              nums[0] = nums[1]*2, nums[2]=nums[1]*2

            Output: 1

        Time Complexity: O(N), where N is the number of elements in nums.
        Space Complexity: O(N), due to auxiliary count storage.
        """
        MOD = 10**9 + 7

        left_c, right_c = Counter([nums[0]]), Counter(nums)
        right_c[nums[0]] -= 1
        special_triplets = 0

        for i in range(1, len(nums) - 1):
            right_c[nums[i]] -= 1

            if left_c.get(nums[i] * 2, 0) > 0 and right_c.get(nums[i] * 2, 0) > 0:
                special_triplets += left_c[nums[i] * 2] * right_c[nums[i] * 2]

            left_c[nums[i]] += 1

        return special_triplets % MOD
