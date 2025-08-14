class Solution:
    def divisorGame(self, n: int) -> bool:
        """
        Determines if Alice wins the Divisor Game given the starting number n.

        Game Description:
            - Alice and Bob take turns; Alice goes first.
            - On each turn, the player chooses any x such that 0 < x < n and n % x == 0.
            - The chosen x is subtracted from n (n becomes n - x).
            - A player loses if they cannot make a move.

        The function returns True if Alice wins, assuming both play optimally.

        Args:
            n (int): The starting number on the chalkboard.

        Returns:
            bool: True if Alice wins, False otherwise.

        Example:
            >>> divisorGame(2)
            True
            >>> divisorGame(3)
            False

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return n % 2 == 0
