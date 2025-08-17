class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        """
        Simulates passing a ball among n children for k seconds, reversing direction at each end.

        There are n children (numbered 0 to n-1) standing in a line. Initially,
        child 0 holds the ball and passes it to the right. Each second, the ball
        is passed to the next child in the current direction. When the ball reaches
        either end (child 0 or child n-1), the direction reverses.

        Args:
            n (int): The number of children in the line.
            k (int): The number of seconds after which to determine the ball's position.

        Returns:
            int: The index of the child holding the ball after k seconds.

        Example:
            >>> numberOfChild(5, 7)
            1

        Time Complexity: O(k)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        rev = False
        i = 0

        while k > 0:
            i += 1 + (-2 * rev)

            if i == n - 1:
                rev = True
            elif i == 0:
                rev = False

            k -= 1

        return i
