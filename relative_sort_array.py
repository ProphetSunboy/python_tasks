class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """
        Given two arrays arr1 and arr2, the elements of arr2 are distinct, and
        all elements in arr2 are also in arr1.

        Sort the elements of arr1 such that the relative ordering of items in
        arr1 are the same as in arr2. Elements that do not appear in arr2 should
        be placed at the end of arr1 in ascending order.

        LeetCode: Beats 96.98%
        """
        sorted_arr1 = sorted(arr1, reverse=True)
        relative_sort = [0] * len(arr1)
        occurs = {}

        j = len(arr1) - 1
        for num in sorted_arr1:
            if num in arr2:
                occurs[num] = occurs.get(num, 0) + 1
            else:
                relative_sort[j] = num
                j -= 1

        for i in range(len(arr2)-1, -1, -1):
            occur = occurs[arr2[i]]
            relative_sort[j-occur+1:j+1] = [arr2[i]] * occur
            j -= occur

        return relative_sort