class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """
        Given an array of distinct integers arr, find all pairs of elements
        with the minimum absolute difference of any two elements.

        Return a list of pairs in ascending order(with respect to pairs),
        each pair [a, b] follows

            a, b are from arr
            a < b
            b - a equals to the minimum absolute difference of any two
            elements in arr

        LeetCode: Beats 91.76%
        """
        sorted_arr = sorted(arr)
        pairs = []
        min_diff = 10 ** 6

        for i, num in enumerate(sorted_arr[1:], 1):
            if num - sorted_arr[i-1] < min_diff:
                pairs = [[sorted_arr[i-1], num]]
                min_diff = num - sorted_arr[i-1]
            elif num - sorted_arr[i-1] == min_diff:
                pairs.append([sorted_arr[i-1], num])

        return pairs