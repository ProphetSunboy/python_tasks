class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        """
        Determines the winner of a bowling game between two players.

        You are given two 0-indexed integer lists player1 and player2, representing
        the number of pins that player 1 and player 2 hit in a bowling game, respectively.

        The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

        Assume a player hits x[i] pins in the ith turn. The value of the ith turn for the player is:
        - 2x[i] if the player hits 10 pins in either (i - 1)th or (i - 2)th turn.
        - Otherwise, it is x[i].

        The score of the player is the sum of the values of their n turns.

        Args:
            player1 (List[int]): List representing pins hit by player 1 in each turn.
            player2 (List[int]): List representing pins hit by player 2 in each turn.

        Returns:
            int: 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw.

        Examples:
            >>> isWinner([4,10,7,9], [6,5,2,3])
            1
            >>> isWinner([3,5,7,6], [8,10,10,2])
            2
            >>> isWinner([2,3], [4,1])
            0

        Time Complexity: O(n) where n is the number of turns
        Space Complexity: O(1)

        LeetCode: Beats 94.32% of submissions
        """
        p1_score = 0
        p2_score = 0

        if len(player1) > 1:
            p1_score += player1[0]
            p2_score += player2[0]

            if player1[0] == 10:
                p1_score += player1[1] * 2
            else:
                p1_score += player1[1]
            if player2[0] == 10:
                p2_score += player2[1] * 2
            else:
                p2_score += player2[1]
        else:
            p1_score = player1[0]
            p2_score = player2[0]

        for i in range(2, len(player1)):
            if player1[i - 1] == 10 or player1[i - 2] == 10:
                p1_score += player1[i] * 2
            else:
                p1_score += player1[i]

        for i in range(2, len(player2)):
            if player2[i - 1] == 10 or player2[i - 2] == 10:
                p2_score += player2[i] * 2
            else:
                p2_score += player2[i]

        if p1_score > p2_score:
            return 1
        elif p1_score < p2_score:
            return 2

        return 0
