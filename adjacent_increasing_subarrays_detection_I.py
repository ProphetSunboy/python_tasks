class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        """
        Determines if there exist two adjacent sublists of length k in `nums`, both of which are strictly increasing.

        Specifically, this checks if there are indices `a` and `b` such that `b = a + k`, and both
        sublists `nums[a..a+k-1]` and `nums[b..b+k-1]` are strictly increasing (each element is less than the next).

        Args:
            nums (List[int]): The input list of integers.
            k (int): The length of the sublists to consider.

        Returns:
            bool: True if such adjacent strictly increasing sublists exist, False otherwise.

        Example:
            >>> hasIncreasingSubarrays([1, 2, 3, 4, 5, 6], 2)
            True
            >>> hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5)
            False

        Time Complexity: O(n*k), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 96.26% of submissions
        """
        for i in range(len(nums) - k * 2 + 1):
            inc = True
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:
                    inc = False
                    break

            if not inc:
                continue

            for j in range(i + k, i + 2 * k - 1):
                if nums[j] >= nums[j + 1]:
                    inc = False
                    break

            if inc:
                return True

        return False
