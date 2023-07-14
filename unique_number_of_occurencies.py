class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        Given an array of integers arr, return true if the number of occurrences
        of each value in the array is unique or false otherwise.

        LeetCode: Beats 99.26%
        """
        occurs = []
        sorted_arr = sorted(arr)
        curr = sorted_arr[0]
        counter = 0

        for num in sorted_arr:
            if num != curr:
                if counter not in occurs:
                    occurs.append(counter)
                else:
                    return False

                curr = num
                counter = 1
            else:
                counter += 1

        if counter in occurs:
            return False

        return True
