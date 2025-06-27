class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        """Transforms the input list nums by:
            1. Replacing each even number with 0.
            2. Replacing each odd number with 1.
            3. Sorting the modified list in non-decreasing order.

        Args:
            nums (list[int]): The list of integers to transform.

        Returns:
            list[int]: The transformed and sorted list.

        Example:
            >>> transformArray([3, 2, 1, 4])
            [0, 0, 1, 1]

        LeetCode: Beats 100% of submissions
        """
        res = []

        even_count = 0
        odd_count = 0

        for num in nums:
            if num % 2:
                odd_count += 1
            else:
                even_count += 1

        res = [0] * even_count + [1] * odd_count

        return res
