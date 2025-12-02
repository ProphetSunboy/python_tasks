class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        Given a 2D integer list points, where points[i] = [xi, yi] represents
        the coordinates of the ith point on the Cartesian plane, this method
        counts the number of unique horizontal trapezoids that can be formed by
        choosing any four distinct points.

        A horizontal trapezoid is defined as a convex quadrilateral that
        contains at least one pair of horizontal (y-equal) sides.

        Returns the total number of such trapezoids modulo 10^9 + 7.

        Args:
            points (List[List[int]]): A list of coordinate pairs.

        Returns:
            int: Number of unique horizontal trapezoids formed from the points,
            modulo 10^9 + 7.

        Example:
            Input: [[1,0],[2,0],[3,0],[2,2],[3,2]]
            Output: 3

        Time Complexity: O(n), where n is the number of points.
        Space Complexity: O(k), where k is the number of unique y-coordinates in
        points.
        """
        point_num = defaultdict(int)
        mod = 10**9 + 7
        ans, total_sum = 0, 0

        for point in points:
            point_num[point[1]] += 1

        for p_num in point_num.values():
            edge = p_num * (p_num - 1) // 2
            ans = (ans + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod

        return ans
