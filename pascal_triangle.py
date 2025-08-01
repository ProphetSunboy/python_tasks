from math import factorial as fact


# First solution
class Solution:
    def binomial_coeff(self, row, col):
        """
        Calculate the binomial coefficients of the given position in
        Pascal's triangle.
        """
        return fact(row) // (fact(col) * fact(row - col))

    def generate(self, numRows: int) -> list[list[int]]:
        """
        Given an integer numRows, return the first numRows of Pascal's triangle.
        """
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i + 1):
                res[i].append(self.binomial_coeff(i, j))

        return res


# Second solution
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """
        Generate the first numRows of Pascal's triangle.

        Each row of Pascal's triangle contains the coefficients of the binomial expansion.
        Each number is the sum of the two numbers directly above it.

        Args:
            numRows (int): The number of rows to generate.

        Returns:
            list[list[int]]: A list of lists representing the first numRows of Pascal's triangle.

        Example:
            >>> generate(5)
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
            ]

        Time complexity: O(numRows^2)
        Space complexity: O(numRows^2)

        LeetCode: Beats 100% of submissions
        """
        triangle = [[1]]

        for i in range(1, numRows):
            triangle.append([1])
            for j in range(1, i):
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            triangle[i].append(1)

        return triangle
