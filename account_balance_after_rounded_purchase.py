class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        """
        Calculates the final bank account balance after making a purchase, rounding
        the purchase amount to the nearest multiple of 10.

        The initial balance is 100 dollars. The purchase amount is rounded to the
        nearest multiple of 10 (rounding up on 5), and this rounded amount is deducted from the balance.

        Args:
            purchaseAmount (int): The amount to spend on a purchase in dollars.

        Returns:
            int: The final bank account balance after the rounded purchase.

        Examples:
            >>> accountBalanceAfterPurchase(9)
            90
            >>> accountBalanceAfterPurchase(15)
            80
            >>> accountBalanceAfterPurchase(4)
            100

        Notes:
            - 0 is considered a multiple of 10.
            - When rounding, 5 is rounded upward (e.g., 5 → 10, 15 → 20, etc.).

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        remainder = purchaseAmount % 10
        purchaseAmount //= 10

        if remainder >= 5:
            purchaseAmount += 1
            purchaseAmount *= 10
        else:
            purchaseAmount *= 10

        return 100 - purchaseAmount
