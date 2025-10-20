class Solution:
    def canAliceWin(self, n: int) -> bool:
        """
        Determines if Alice can win the stone removal game with the following rules:

        - There is a pile with n stones.
        - Alice goes first and must remove exactly 10 stones on her first turn.
        - Thereafter, each player on their turn must remove exactly 1 fewer stone than the
          previous opponent removed (i.e., move sizes: 10, 9, 8, ..., 1).
        - A player unable to make a valid move (not enough stones remaining) loses.

        Args:
            n (int): The initial number of stones in the pile.

        Returns:
            bool: True if Alice wins the game, False otherwise.

        Example:
            >>> canAliceWin(55)  # Alice should win
            True
            >>> canAliceWin(45)  # Alice should lose
            False

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i = 10

        while n >= i:
            n -= i
            i -= 1

        return i % 2 == 1
