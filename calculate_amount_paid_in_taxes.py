class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        """Calculates the total tax paid based on tax brackets and income.

        Given a list of tax brackets and an income, this function computes the total amount of tax to be paid.
        Each bracket is defined by an upper income limit and a tax percentage. The tax is calculated progressively:
        for each bracket, only the portion of income within that bracket is taxed at the bracket's rate.

        Args:
            brackets (List[List[int]]): A list where each element is [upper, percent], representing the upper bound
                of the bracket and the tax percentage for that bracket.
            income (int): The total income to calculate taxes for.

        Returns:
            float: The total tax paid.

        Example:
            >>> calculateTax([[3,50],[7,10],[12,25]], 10)
            2.65000

        Time complexity: O(n), where n is the number of tax brackets.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        taxes = 0
        prev_upper = 0
        i = 0

        while income > 0:
            curr = brackets[i][0] - prev_upper
            if curr < income:
                taxes += curr * (brackets[i][1] / 100)
                income -= curr
            else:
                taxes += income * (brackets[i][1] / 100)
                income -= income

            prev_upper = brackets[i][0]
            i += 1

        return taxes
