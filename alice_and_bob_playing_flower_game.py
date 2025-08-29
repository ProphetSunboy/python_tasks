class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        Alice and Bob are playing a turn-based game with two lanes of flowers.
        There are x flowers in the first lane and y flowers in the second lane.

        Game rules:
            - Alice goes first.
            - On each turn, a player picks one flower from either lane.
            - The player who picks the last flower wins.

        Given two integers n and m, representing the maximum possible number of flowers
        in the first and second lanes respectively, compute the number of pairs (x, y) such that:
            - 1 <= x <= n
            - 1 <= y <= m
            - Alice wins the game if both play optimally.

        Args:
            n (int): Maximum number of flowers in the first lane.
            m (int): Maximum number of flowers in the second lane.

        Returns:
            int: The number of (x, y) pairs where Alice wins.

        Example:
            >>> flowerGame(3, 2)
            3

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        pairs = 0

        for i in range(1, n + 1):
            if i % 2 == 0:
                if m % 2:
                    pairs += (m - 1) // 2 + 1
                else:
                    pairs += m // 2
            else:
                pairs += m // 2

        return pairs
