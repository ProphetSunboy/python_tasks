class Solution:
    def max_in_column(self, matrix: list[list[int]], j: int, min_r: int) -> bool:
        """
        Check if a value is the maximum in its column.

        Args:
            matrix (list[list[int]]): The input matrix
            j (int): Column index to check
            min_r (int): Value to compare against - should be minimum in its row

        Returns:
            bool: True if min_r is maximum in column j, False otherwise

        Time complexity: O(m) where m is number of rows
        Space complexity: O(1)
        """
        for i in range(len(matrix)):
            if matrix[i][j] > min_r:
                return False

        return True

    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        """
        Find all lucky numbers in a matrix.

        A lucky number is an element that is both the minimum in its row and maximum in its column.

        Args:
            matrix (List[List[int]]): m x n matrix of distinct integers

        Returns:
            List[int]: List of lucky numbers found in the matrix

        Time complexity: O(m*n) where m is number of rows and n is number of columns
        Space complexity: O(k) where k is number of lucky numbers found

        LeetCode: Beats 100% of submissions
        """
        lucky = []

        for i in range(len(matrix)):
            m = matrix[i][0]
            idx = 0

            for j in range(len(matrix[0])):
                if matrix[i][j] < m:
                    m = matrix[i][j]
                    idx = j

            if self.max_in_column(matrix, idx, m):
                lucky.append(m)

        return lucky
