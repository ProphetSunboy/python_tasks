class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        Given an integer list nums and an integer list queries, for each query queries[i],
        return the maximum size of a subsequence from nums such that the sum of its elements
        is less than or equal to queries[i].

        A subsequence is a list that can be derived from another list by deleting some or
        no elements without changing the order of the remaining elements.

        Args:
            nums (list[int]): The input list of integers.
            queries (list[int]): The list of query sums.

        Returns:
            list[int]: For each query, the maximum length of a subsequence whose sum is
            less than or equal to the query value.

        Example:
            >>> answerQueries([4,5,2,1], [3,10,21])
            [2, 3, 4]
            >>> answerQueries([2,3,4,5], [1])
            [0]

        Time complexity: O(n log n + m log m), where n is the length of nums and m is the length of queries.
        Space complexity: O(m + n).

        LeetCode: Beats 98.64% of submissions
        """
        nums.sort()
        sorted_q = sorted(queries)
        vals = dict()

        curr_sum = 0
        curr_len = 0
        i, j = 0, 0
        while i < len(nums) and j < len(sorted_q):
            if curr_sum > sorted_q[j]:
                vals[sorted_q[j]] = curr_len - 1
                j += 1
            elif curr_sum == sorted_q[j]:
                vals[sorted_q[j]] = curr_len
                j += 1
            else:
                curr_sum += nums[i]
                curr_len += 1
                i += 1

        for k in range(j, len(sorted_q)):
            if curr_sum > sorted_q[k]:
                vals[sorted_q[k]] = curr_len - 1
            else:
                vals[sorted_q[k]] = curr_len

        ans = [vals.get(q) for q in queries]

        return ans
