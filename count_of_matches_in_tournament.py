class Solution:
    def numberOfMatches(self, n: int) -> int:
        """Calculates the total number of matches played in a tournament.

        Given `n` teams, the function simulates a tournament with specific rules:
        - If the number of teams is even, `n / 2` matches are played, and `n / 2` teams advance.
        - If the number of teams is odd, `(n - 1) / 2` matches are played, and `(n - 1) / 2 + 1` teams advance.
        The simulation continues until one winner is decided.

        Args:
            n (int): The initial number of teams in the tournament.

        Returns:
            int: The total number of matches played.

        Example:
            Input: n = 7
            Output: 6
            Explanation:
            - Round 1: Teams = 7, Matches = 3, Teams advancing = 4
            - Round 2: Teams = 4, Matches = 2, Teams advancing = 2
            - Round 3: Teams = 2, Matches = 1, Winner decided
            Total matches = 3 + 2 + 1 = 6.

        Time complexity: O(log N), where N is the number of teams, as N is
                       roughly halved in each iteration.
        Space complexity: O(1), as only a few variables are used.

        LeetCode: Beats 96.98% of submissions
        """
        played = 0

        while n > 1:
            if n % 2:
                played += (n - 1) // 2
                n = (n - 1) // 2 + 1
            else:
                n //= 2
                played += n

        return played
