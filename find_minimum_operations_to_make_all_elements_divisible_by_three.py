class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Given an integer list nums, you can perform the following operation any number of times:
        - Add or subtract 1 from any element of nums.

        Return the minimum total number of operations required to make every element in nums divisible by 3.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum number of operations needed.

        Example:
            >>> minimumOperations([2, 3, 4])
            2

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissionss
        """
        ops = 0

        for num in nums:
            i = 0
            while (num + i) % 3:
                i += 1

            j = 0
            while (num - j) % 3:
                j += 1

            ops += min(i, j)

        return ops
