class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        """
        You are given an integer list arr. Sort the integers in the list in
        ascending order by the number of 1's in their binary representation and
        in case of two or more integers have the same number of 1's you have to
        sort them in ascending order.

        :param list[int] arr: integer list
        :returns list[int] lst: arr sorted by the number of 1's in their binary
        representation

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 97.69%
        """
        lst = [(bin(num).count("1"), num) for num in arr]

        lst.sort()

        return [l[1] for l in lst]
