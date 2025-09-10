class Solution:
    def numberOfCuts(self, n: int) -> int:
        """
        Calculates the minimum number of straight cuts required to divide a circle into n equal slices.

        A valid cut is a straight line passing through the center of the circle, either:
            - Connecting two points on the edge (diameter cut), or
            - Passing through the center and touching a single point on the edge (radius cut).

        Args:
            n (int): The number of equal slices to divide the circle into.

        Returns:
            int: The minimum number of cuts needed.

        Examples:
            >>> numberOfCuts(4)
            2
            >>> numberOfCuts(3)
            3
            >>> numberOfCuts(1)
            0

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        if n == 1:
            return 0

        return n if n % 2 else n // 2
