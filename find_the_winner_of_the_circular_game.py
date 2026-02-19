class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Simulates a circular elimination game to find the winner.

        There are n friends sitting in a circle, numbered from 1 to n in clockwise order.
        The game proceeds as follows:
            1. Start at the 1st friend.
            2. Count the next k friends in the clockwise direction, including the current one.
               Counting wraps around the circle if needed.
            3. The k-th friend counted leaves the circle.
            4. Repeat from the next clockwise friend until only one remains.

        Args:
            n (int): The number of friends in the circle.
            k (int): The step count for each elimination.

        Returns:
            int: The number of the friend who wins the game.

        Example:
            Input: n = 5, k = 2
            Output: 3

        Time Complexity: O(n), as each elimination takes O(1) and n-1 eliminations occur.
        Space Complexity: O(n), due to the list of players.

        LeetCode: Beats 100% of submissions
        """
        players = [i for i in range(1, n + 1)]
        curr_pos = 0

        while len(players) > 1:
            curr_pos = (curr_pos + k - 1) % len(players)

            players.pop(curr_pos)
            if curr_pos == len(players):
                curr_pos = 0

        return players[0]
