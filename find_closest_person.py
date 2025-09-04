class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """
        Determines which of two people reaches a third person first on a number line.

        Given:
            x (int): Position of Person 1.
            y (int): Position of Person 2.
            z (int): Position of Person 3 (stationary).

        Both Person 1 and Person 2 move toward Person 3 at the same speed.

        Returns:
            int: 1 if Person 1 arrives first,
                 2 if Person 2 arrives first,
                 0 if both arrive at the same time.

        Example:
            >>> findClosest(1, 4, 2)
            1

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        x_dist = abs(z - x)
        y_dist = abs(z - y)

        if x_dist < y_dist:
            return 1
        elif x_dist > y_dist:
            return 2

        return 0
