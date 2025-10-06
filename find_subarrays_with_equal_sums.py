class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        """
        Determines if there exist two distinct sublists of length 2 in the input list `nums` that have the same sum.

        Args:
            nums (List[int]): A 0-indexed list of integers.

        Returns:
            bool: True if there are at least two sublists of length 2 with equal sum, False otherwise.

        Example:
            >>> findSubarrays([4, 2, 4])
            True
            >>> findSubarrays([1, 2, 3, 4, 5])
            False

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), for storing seen sums.

        LeetCode: Beats 100% of submissions
        """
        seen = set()

        for i in range(2):
            for j in range(i, len(nums) - 1, 2):

                curr_sum = nums[j] + nums[j + 1]
                if curr_sum in seen:
                    return True

                seen.add(curr_sum)

        return False
