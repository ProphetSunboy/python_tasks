class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        """Calculate the maximum wealth among all customers.

        You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
        the i-th customer has in the j-th bank. Return the wealth that the richest customer has.

        A customer's wealth is the amount of money they have in all their bank accounts.
        The richest customer is the customer that has the maximum wealth.

        Args:
            accounts (list[list[int]]): Grid where accounts[i][j] represents money in customer i's account j

        Returns:
            int: The maximum wealth among all customers

        Example:
            >>> maximumWealth([[1,2,3],[3,2,1]])
            6
            >>> maximumWealth([[1,5],[7,3],[3,5]])
            10

        Time complexity: O(m*n) where m is number of customers and n is number of accounts
        Space complexity: O(1) since we only store the running maximum

        LeetCode: Beats 100% of submissions
        """
        return max([sum(row) for row in accounts])
