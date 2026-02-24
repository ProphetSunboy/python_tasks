class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer list nums of unique elements, return all possible
        subsets (the power set).

        The solution set must not contain duplicate subsets.
        Return the solution in any order.

        Args:
            nums (List[int]): List of unique integers.

        Returns:
            List[List[int]]: A list containing all possible subsets.

        Example:
            Input: nums = [1, 2, 3]
            Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

        Time Complexity: O(2^n), where n is the length of nums.
        Space Complexity: O(2^n), for storing all subsets.

        LeetCode: Beats 100% of submissions
        """
        subsets = [[]]

        for num in nums:
            curr = []
            for subset in subsets:
                curr.append(subset + [num])

            subsets += curr

        return subsets
