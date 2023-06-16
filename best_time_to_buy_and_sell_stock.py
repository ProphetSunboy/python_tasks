class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given an array prices where prices[i] is the price of a given stock on
        the ith day.

        Function maximize profit by choosing a single day to buy one stock and
        choosing a different day in the future to sell that stock.

        Return the maximum profit that can be achieved from this transaction.
        If any profit cannot achieved, return 0.
        """
        max_profit = 0
        min_buy = max(prices)
        for i in range(len(prices)-1):
            if prices[i] < min_buy and prices[i] < prices[i+1]:
                profit = max(prices[i+1:]) - prices[i]
                if profit > max_profit:
                    max_profit = profit
                min_buy = prices[i]
        
        return max_profit