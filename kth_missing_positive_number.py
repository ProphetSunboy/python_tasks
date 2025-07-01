class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        """Given a sorted list `arr` of positive integers (strictly increasing) and an integer `k`,
        return the k-th positive integer that is missing from this list.

        Args:
            arr (list[int]): The sorted list of positive integers.
            k (int): The k-th missing positive number to find.

        Returns:
            int: The k-th missing positive integer.

        Example:
            >>> findKthPositive([2, 3, 4, 7, 11], 5)
            9
            >>> findKthPositive([1, 2, 3, 4], 2)
            6

        LeetCode: Beats 100% of submissions
        """
        i = 0
        j = 0
        int_row = list(range(1, arr[-1] + k + 1))
        arr += [0] * (len(int_row) - len(arr))

        while k > 0:
            if int_row[i] == arr[j]:
                i += 1
                j += 1
            else:
                i += 1
                k -= 1

        return int_row[i - 1]
