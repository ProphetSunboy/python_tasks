class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """Calculate final prices with special discounts for items in a shop.

        For each item, apply a discount equal to the price of the first subsequent item
        that has a price less than or equal to the current item's price. If no such item
        exists, no discount is applied.

        Args:
            prices (list[int]): List of item prices in the shop

        Returns:
            list[int]: List of final prices after applying discounts

        Example:
            >>> finalPrices([8,4,6,2,3])
            [4,2,4,2,3]  # 8-4=4, 4-2=2, 6-2=4, 2-0=2, 3-0=3

        Time complexity: O(n²) - nested loops comparing each price with subsequent prices
        Space complexity: O(n) - stores result list of same length as input

        LeetCode: Beats 100% of submissions
        """
        answer = []

        for i, price in enumerate(prices):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    discount = prices[j]
                    break

            answer.append(price - discount)

        return answer
