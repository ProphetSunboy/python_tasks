class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        """
        Check if list contains a number and its double.

        Given a list arr of integers, checks if there exist two indices i and j such that:
        - i != j (different indices)
        - 0 <= i, j < arr.length (valid indices)
        - arr[i] == 2 * arr[j] (one number is double the other)

        Args:
            arr (List[int]): list of integers to check

        Returns:
            bool: True if a number and its double exist, False otherwise

        Time complexity: O(n) where n is length of input list
        Space complexity: O(n) for the hash table

        LeetCode: Beats 100% of submissions
        """
        d = {}

        for num in arr:
            if d.get(num * 2, 0) or d.get(num / 2, 0):
                return True

            d[num] = 1

        return False
