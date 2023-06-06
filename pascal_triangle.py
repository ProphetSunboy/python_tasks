from math import factorial as fact

class Solution:
    def binomial_coeff(self, row, col):
        """
        Calculate the binomial coefficients of the given position in
        Pascal's triangle.
        """
        return fact(row) // (fact(col) * fact(row - col))

    def generate(self, numRows: int) -> List[List[int]]:
        """
        Given an integer numRows, return the first numRows of Pascal's triangle.
        """
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i+1):
                res[i].append(self.binomial_coeff(i, j))

        return res