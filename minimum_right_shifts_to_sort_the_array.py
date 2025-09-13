class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        """
        Given a 0-indexed list nums of length n containing distinct positive integers,
        return the minimum number of right shifts required to sort nums in ascending order.
        If it is not possible to sort the list by any number of right shifts, return -1.

        A right shift is defined as moving the element at index i to index (i + 1) % n for all indices.

        Args:
            nums (List[int]): The input list of distinct positive integers.

        Returns:
            int: The minimum number of right shifts needed to sort the list, or -1 if impossible.

        Examples:
            >>> minimumRightShifts([3, 4, 5, 1, 2])
            2
            >>> minimumRightShifts([1, 3, 5])
            0
            >>> minimumRightShifts([2, 1, 4])
            -1

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i = len(nums) - 1

        while i >= 0:
            if nums[i] <= nums[(i - 1 + len(nums)) % len(nums)]:
                break
            i -= 1

        if i == 0:
            return 0

        for n in range(i + 1, i + len(nums)):
            print(nums[n % len(nums)])
            if nums[n % len(nums)] < nums[(n % len(nums)) - 1]:
                return -1

        return len(nums) - i
