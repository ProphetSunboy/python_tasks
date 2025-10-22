class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        """
        Find all the losers in the circular passing game.

        There are n friends sitting in a circle, numbered from 1 to n clockwise.
        - The 1st friend starts with the ball.
        - On the ith turn, the current holder passes the ball to the friend who is i * k steps
          away in the clockwise direction (wrapping around as needed).
        - The game ends when a friend receives the ball for the second time.
        - Losers are friends who never received the ball during the entire game.

        Args:
            n (int): Number of friends in the circle.
            k (int): Step size for passing the ball.

        Returns:
            List[int]: Sorted list of friends (1-indexed) who never received the ball.

        Example:
            >>> circularGameLosers(5, 2)
            [4, 5]

        Time Complexity: O(n), where n is the number of friends.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        friends = [False] * n

        i = 0
        j = 1
        while not friends[i]:
            friends[i] = True
            i = (i + j * k) % n
            j += 1

        return [f + 1 for f in range(len(friends)) if not friends[f]]
