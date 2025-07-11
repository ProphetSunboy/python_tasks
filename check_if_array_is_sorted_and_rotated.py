class Solution:
    def check(self, nums: list[int]) -> bool:
        """Determines if the given list was originally sorted in non-decreasing order and then rotated.

        A list is considered sorted and rotated if it can be obtained by rotating a non-decreasingly sorted list
        any number of times (including zero). Duplicates are allowed.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            bool: True if the list is sorted and rotated, False otherwise.

        Example:
            >>> check([3, 4, 5, 1, 2])
            True
            >>> check([2, 1, 3, 4])
            False

        Note:
            Rotating an array A by x positions results in an array B such that
            B[i] == A[(i + x) % len(A)] for every valid index i.

        Time complexity: O(n), where n is the length of the input list.
        Space complexity: O(n), due to sorting and auxiliary storage.

        LeetCode: Beats 100% of submissions
        """
        s_nums = sorted(nums)
        k = 0

        while k < len(nums):
            flag = True
            for i in range(len(nums)):
                if nums[(i + k) % len(nums)] != s_nums[i]:
                    flag = False
                    break

            if flag:
                return True

            k += 1

        return False
