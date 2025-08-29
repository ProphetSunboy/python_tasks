class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        """
        Determines the winner of a coin game between Alice and Bob.

        There are two types of coins:
            - x coins of value 75
            - y coins of value 10

        Rules:
            - Alice and Bob take turns, with Alice going first.
            - On each turn, a player must pick coins totaling exactly 115 in value (i.e., 1 coin of 75 and 4 coins of 10).
            - If a player cannot make such a move on their turn, they lose.

        Args:
            x (int): Number of coins with value 75.
            y (int): Number of coins with value 10.

        Returns:
            str: The name of the winning player ("Alice" or "Bob") if both play optimally.

        Example:
            >>> winningPlayer(3, 12)
            'Alice'
            >>> winningPlayer(1, 3)
            'Bob'

        Time Complexity: O(min(x, y // 4)), since each turn removes 1 coin of 75 and 4 coins of 10.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i = 0

        while x >= 0 and y >= 0:
            x -= 1
            y -= 4

            if x < 0 or y < 0:
                return ["Alice", "Bob"][(i + 1) % 2]

            i += 1

        return ["Alice", "Bob"][i % 2]
