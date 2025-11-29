class Solution:
    def minOperations(self, n: int) -> int:
        """
        Given an integer n, this function computes the minimum number of operations
        required to make all elements of a list equal, where the list is defined as:
            arr[i] = 2 * i + 1  for i in 0..n-1

        In one operation, you can pick any two indices x and y (0 <= x, y < n),
        subtract 1 from arr[x] and add 1 to arr[y].

        Args:
            n (int): The number of elements in the list

        Returns:
            int: The minimum number of operations needed to make all the
            elements of arr equal.

        Example:
            Input: n = 3
            arr = [1, 3, 5]
            Output: 2
            Explanation:
                - [1,3,5] -> [2,3,4] -> [3,3,3] (2 operations)

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return (n**2) // 4
