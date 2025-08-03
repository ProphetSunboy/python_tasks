class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        """
        Distributes elements of the input list `nums` into two lists, `arr1` and `arr2`, according to the following rules:

        - The first element (nums[0]) is appended to arr1.
        - The second element (nums[1]) is appended to arr2.
        - For each subsequent element nums[i] (i >= 2):
            - If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1.
            - Otherwise, append nums[i] to arr2.

        The final result is the concatenation of arr1 followed by arr2.

        Args:
            nums (list[int]): A list of distinct integers.

        Returns:
            list[int]: The concatenated list formed by arr1 + arr2.

        Example:
            >>> resultArray([2, 1, 3, 4, 5])
            [2, 3, 4, 5, 1]

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
