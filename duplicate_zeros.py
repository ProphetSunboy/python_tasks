class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Given a fixed-length integer list arr, duplicate each occurrence of
        zero, shifting the remaining elements to the right.

        Note that elements beyond the length of the original array are not
        written. Do the above modifications to the input list in place and do
        not return anything.

        :param list[int] arr: fixed-length integer list
        :returns None

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 95.15%
        """
        duplicate = arr[::]
        i = j = 0

        while i < len(duplicate):
            if duplicate[j] == 0:
                arr[i] = 0
                if i + 1 < len(duplicate):
                    arr[i + 1] = 0
                i += 1
            else:
                arr[i] = duplicate[j]

            i += 1
            j += 1
