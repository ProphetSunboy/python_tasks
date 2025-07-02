class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        """Given a binary list nums and an integer k, return True if all 1's are
        at least k places away from each other, otherwise return False.

        Args:
            nums (list[int]): The binary list to check.
            k (int): The minimum required distance between consecutive 1's.

        Returns:
            bool: True if all 1's are at least k places apart, False otherwise.

        Example:
            >>> kLengthApart([1,0,0,0,1,0,0,1], 2)
            True
            >>> kLengthApart([1,0,0,1,0,1], 2)
            False

        LeetCode: Beats 93.98% of submissions
        """
        prev_1 = -(10**5)

        for i, num in enumerate(nums):
            if num == 1:
                if i - prev_1 - 1 < k:
                    return False
                prev_1 = i

        return True
