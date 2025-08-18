class Solution:
    def distMoney(self, money: int, children: int) -> int:
        """
        Distributes a given amount of money among a specified number of children according to the following rules:
            - All money must be distributed.
            - Each child must receive at least 1 dollar.
            - No child can receive exactly 4 dollars.

        Returns the maximum number of children who can receive exactly 8 dollars.
        If it is not possible to distribute the money according to the rules, returns -1.

        Args:
            money (int): The total amount of money to distribute.
            children (int): The number of children to distribute the money to.

        Returns:
            int: The maximum number of children who can receive exactly 8 dollars, or -1 if not possible.

        Example:
            >>> distMoney(20, 3)
            1

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        if children > money:
            return -1

        money -= children
        eights = 0

        while money >= 7 and eights < children - 1:
            eights += 1
            money -= 7

        if money == 3 and children - eights < 2:
            eights -= 1
        elif money == 7:
            eights += 1

        return eights
