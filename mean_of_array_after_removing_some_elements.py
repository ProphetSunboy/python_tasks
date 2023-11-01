class Solution:
    def trimMean(self, arr: list[int]) -> float:
        """
        Given an integer list arr, return the mean of the remaining integers
        after removing the smallest 5% and the largest 5% of the elements.

        :param list[int] arr: integer list
        :returns float mean: mean of the remaining integers of arr after
        removing the smallest 5% and the largest 5% of the elements

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 98.23%
        """
        lst = sorted(arr)
        i = len(lst) // 20

        return sum(lst[i:-i]) / (len(lst) - 2 * i)
