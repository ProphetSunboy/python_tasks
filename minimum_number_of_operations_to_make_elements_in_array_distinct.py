class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Given an integer list nums, return the minimum number of operations required to make all elements in the list distinct.
        In one operation, remove the first 3 elements from the list (or remove all remaining elements if fewer than 3 remain).
        An empty list is considered to have all distinct elements.

        Args:
            nums (List[int]): The list of integers to process.

        Returns:
            int: The minimum number of operations needed to make all elements distinct.

        Example:
            >>> minimumOperations([1, 2, 2, 3])
            1

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        seen = [False] * 128
        for i in range(len(nums) - 1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
        return 0
