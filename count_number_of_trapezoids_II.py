class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        Given a list of 2D points on the Cartesian plane, returns the number of unique trapezoids
        that can be formed by choosing any four distinct points from the list.

        A trapezoid is defined as a convex quadrilateral with at least one pair of parallel sides.
        Two sides are parallel if they have the same slope.

        Args:
            points (List[List[int]]): A list of [x, y] coordinate pairs.

        Returns:
            int: The number of unique trapezoids that can be formed.

        Example:
            Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
            Output: 2

        Time Complexity: O(N^2), where N is the number of points (for enumerating all line segments).
        Space Complexity: O(N^2), for storing slopes and intercepts.

        LeetCode: Beats 99.49% of submissions
        """
        n = len(points)
        inf = 10**9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        ans = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2

                if x2 == x1:
                    k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx

                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)

        for sti in slope_to_intercept.values():
            if len(sti) == 1:
                continue

            cnt = defaultdict(int)
            for b_val in sti:
                cnt[b_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans += total_sum * count
                total_sum += count

        for mts in mid_to_slope.values():
            if len(mts) == 1:
                continue

            cnt = defaultdict(int)
            for k_val in mts:
                cnt[k_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans -= total_sum * count
                total_sum += count

        return ans
