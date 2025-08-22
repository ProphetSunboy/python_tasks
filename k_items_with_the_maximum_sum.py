class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        """
        Given a bag containing items labeled with 1, 0, or -1, determine the maximum possible sum by picking exactly k items.

        Args:
            numOnes (int): Number of items labeled 1.
            numZeros (int): Number of items labeled 0.
            numNegOnes (int): Number of items labeled -1.
            k (int): Number of items to pick.

        Returns:
            int: The maximum possible sum obtainable by picking k items.

        Example:
            >>> kItemsWithMaximumSum(3, 2, 0, 2)
            2
            >>> kItemsWithMaximumSum(3, 2, 0, 4)
            3
            >>> kItemsWithMaximumSum(1, 1, 3, 4)
            -2

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        if numOnes >= k:
            return k
        elif numOnes + numZeros >= k:
            return min(numOnes, k)
        else:
            return numOnes - (k - numOnes - numZeros)
