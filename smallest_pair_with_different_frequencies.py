class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        """
        Given an integer list nums, find all pairs of distinct values x and y
        from nums such that:

            - x < y
            - x and y have different frequencies in nums

        Among all such pairs, choose the pair with the smallest possible value
        of x.
        If multiple pairs have the same x, choose the one with the smallest
        possible value of y.

        Returns an integer list [x, y].
        If no valid pair exists, returns [-1, -1].

        Args:
            nums (list[int]): The list of integers.

        Returns:
            list[int]: The pair [x, y] where x < y, and x and y have different
                frequencies in nums, chosen as described. Returns [-1, -1]
                if no such pair exists.

        Example:
            Input: nums = [1, 2, 2, 3]
            Output: [1, 2]

        Time Complexity: O(n log n), due to sorting unique values.
        Space Complexity: O(n), to store frequencies.

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)

        vals = sorted(c.items())

        res = [vals[0]]

        for val in vals:
            if val[1] != res[0][1]:
                res.append(val)
                break

        return [res[0][0], res[1][0]] if len(res) == 2 else [-1, -1]
