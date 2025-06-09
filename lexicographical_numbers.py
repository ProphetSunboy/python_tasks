# First attempt
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        """Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

        Args:
            n (int): The upper bound of the range [1, n]

        Returns:
            list[int]: A list of integers from 1 to n sorted in lexicographical order

        Example:
            >>> lexicalOrder(13)
            [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

        Time complexity: O(n log n) - due to sorting
        Space complexity: O(n) - for storing the result list
        """
        return list(map(int, sorted(map(str, range(1, n + 1)))))


# Second attempt
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        """Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

        Args:
            n (int): The upper bound of the range [1, n]

        Returns:
            list[int]: A list of integers from 1 to n sorted in lexicographical order

        Example:
            >>> lexicalOrder(13)
            [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

        Time complexity: O(n log n) - due to sorting
        Space complexity: O(n) - for storing the result list

        LeetCode: Beats 95.39% of submissions
        """
        return sorted(range(1, n + 1), key=str)
