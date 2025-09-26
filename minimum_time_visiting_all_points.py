class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Calculates the minimum time required to visit all points in order on a 2D plane.

        You start at the first point and must visit each subsequent point in order.
        In 1 second, you can move:
            - Vertically by one unit,
            - Horizontally by one unit,
            - Or diagonally by one unit in both directions (i.e., (x+1, y+1) or (x-1, y-1)).

        The minimum time to move from one point to another is the maximum of the differences
        in their x and y coordinates.

        Args:
            points (List[List[int]]): List of points, where each point is [x, y].

        Returns:
            int: The minimum time in seconds to visit all points in order.

        Example:
            >>> minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
            7
            # Explanation: Move from (1,1) to (3,4) in 3 seconds, then to (-1,0) in 4 seconds.

        Time Complexity: O(N), where N is the number of points.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        time = 0
        curr_point = points[0]

        for i in range(1, len(points)):
            time += max(
                abs(curr_point[0] - points[i][0]), abs(curr_point[1] - points[i][1])
            )
            curr_point = points[i]

        return time
