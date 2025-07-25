class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        """Given a 2D integer list nums where each nums[i] is a non-empty list of
        distinct positive integers, return a sorted list of integers that are present
        in every list of nums.

        Args:
            nums (list[list[int]]): A list of lists, where each sublist contains distinct positive integers.

        Returns:
            list[int]: Sorted list of integers present in all sublists of nums.

        Example:
            >>> intersection([[1,2,3],[2,3,4],[2,3]])
            [2, 3]

        Time complexity: O(n * m), where n is the number of sublists and m is the average length of a sublist.
        Space complexity: O(m), for storing the intersection.

        LeetCode: Beats 100% of submissions
        """
        inter = {nums[0][i]: 1 for i in range(len(nums[0]))}

        for i in range(1, len(nums)):
            for num in nums[i]:
                if inter.get(num, 0):
                    inter[num] += 1

        max_val = max(inter.values())
        res = []

        if max_val != len(nums):
            return []

        for num, val in inter.items():
            if val == max_val:
                res.append(num)

        return sorted(res)
