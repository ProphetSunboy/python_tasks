class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        """
        Calculates the sum of the squares of the number of distinct elements for all sublists of nums.

        A sublist is a contiguous non-empty sequence of elements within the list.
        For each sublist nums[i..j], compute the number of distinct elements, square it, and sum over all sublists.

        Args:
            nums (list[int]): The input integer list.

        Returns:
            int: The sum of the squares of the counts of distinct elements for all sublists.

        Example:
            >>> sumCounts([1,2,1])
            15
            # Explanation:
            # Sublists and their distinct counts:
            # [1] -> 1^2 = 1
            # [1,2] -> 2^2 = 4
            # [1,2,1] -> 2^2 = 4
            # [2] -> 1^2 = 1
            # [2,1] -> 2^2 = 4
            # [1] -> 1^2 = 1
            # Total = 1 + 4 + 4 + 1 + 4 + 1 = 15

        Time Complexity: O(n^2)
        Space Complexity: O(n)

        LeetCode: Beats 94.89% of submissions
        """
        s_sqr = 0

        for i in range(len(nums)):
            distinct_nums = set()
            for j in range(i, len(nums)):
                distinct_nums.add(nums[j])
                s_sqr += len(distinct_nums) ** 2

        return s_sqr
