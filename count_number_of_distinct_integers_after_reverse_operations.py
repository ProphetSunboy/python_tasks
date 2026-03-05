class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        """
        Given a list `nums` of positive integers, for each integer add its
        digit-reversed value to the list (apply this operation only to the
        original elements in `nums`).
        Return the number of distinct integers in the resulting list.

        Args:
            nums (List[int]): List of positive integers.

        Returns:
            int: Number of distinct integers after adding reversed values.

        Example:
            Input: nums = [1, 13, 10, 12, 31]
            Output: 6
            Explanation: After reversing and adding, the list becomes
            [1, 13, 10, 12, 31, 1, 31, 1, 21, 13].
            The distinct numbers are {1, 10, 12, 13, 21, 31}.

        Time Complexity: O(n), where n is the number of elements in nums.
        Space Complexity: O(n), for storing distinct values.

        LeetCode: Beats 90.95% of submissions
        """
        unique_orig = set(nums)

        reversed_nums = [int(str(x)[::-1]) for x in unique_orig]

        unique_orig.update(reversed_nums)

        return len(unique_orig)
