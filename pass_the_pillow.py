class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """Simulates passing a pillow among n people standing in a line, labeled from 1 to n.

        The first person (index 1) starts with the pillow. Every second, the pillow is passed to the next person in the current direction.
        When the pillow reaches either end of the line (person 1 or person n), the direction reverses.

        Args:
            n (int): The number of people in the line.
            time (int): The number of seconds after which to determine who holds the pillow.

        Returns:
            int: The index (1-based) of the person holding the pillow after 'time' seconds.

        Example:
            >>> passThePillow(4, 5)
            2

        Time complexity: O(time)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i = 1

        reverse = False
        while time > 0:
            if reverse:
                i -= 1

                if i == 1:
                    reverse = False
            else:
                i += 1

                if i == n:
                    reverse = True

            time -= 1

        return i
