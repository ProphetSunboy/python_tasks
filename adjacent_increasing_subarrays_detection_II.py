class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        """
        Finds the maximum length k for which there exist two adjacent, strictly
        increasing sublists of length k each in nums.

        For an integer list nums, looks for the largest k such that there exist indices a (0 <= a < n-2k+1)
        and b = a + k with:
            - nums[a..a+k-1] is strictly increasing
            - nums[b..b+k-1] is strictly increasing

        The sublists must be contiguous and non-overlapping.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The maximum possible value of k such that two adjacent strictly increasing sublists of length k exist.

        Example:
            >>> maxIncreasingSubarrays([1, 2, 3, 4, 5])
            2   # [1,2],[3,4] and [2,3],[4,5] are both increasing pairs
            >>> maxIncreasingSubarrays([1, 2, 1, 2, 3])
            2   # The subarrays [1,2] and [1,2] or [1,2] and [2,3]
            >>> maxIncreasingSubarrays([5, 4, 3, 2])
            1

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)
        """
        n = len(nums)
        cnt, precnt, ans = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                precnt, cnt = cnt, 1
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans
