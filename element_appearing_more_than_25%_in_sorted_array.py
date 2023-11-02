class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        """
        Given an integer list sorted in non-decreasing order, there is exactly
        one integer in the list that occurs more than 25% of the time, return
        that integer.

        :param list[int] arr: sorted in non-decreasing order integer list
        :returns int num: number in the arr that occurs more than 25% of the time

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 96.63%
        """
        per = len(arr) // 4

        for i in range(len(arr)):
            if arr[i] == arr[i + per]:
                return arr[i]
