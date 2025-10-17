class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Given an integer list nums and an integer k, return the minimum number of operations required
        to make every element in nums equal to k using the allowed operation, or -1 if impossible.

        Operation:
            - Choose a valid integer h. h is considered valid if all values in nums strictly greater than h are identical.
            - For every index i where nums[i] > h, set nums[i] = h.

        The goal is to transform nums so that every element equals k using the
        fewest number of operations.

        Args:
            nums (List[int]): The initial list of integers.
            k (int): The target integer value for all elements.

        Returns:
            int: The minimum number of operations to achieve the goal, or -1 if it is impossible.

        Example:
            >>> minOperations([10, 8, 10, 8], 8)
            1
            >>> minOperations([5, 5, 5], 4)
            1

        Time Complexity: O(n log n), due to sorting the unique values in nums.
        Space Complexity: O(n), for storing unique elements.

        LeetCode: Beats 97.52% of submissions
        """
        unique_nums = sorted(set(nums), reverse=True)

        if unique_nums[-1] < k:
            return -1

        if unique_nums[-1] != k:
            return len(unique_nums)

        return len(unique_nums) - 1
