class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        """
        Given n rectangles in a 2D plane with edges parallel to the x and y axes,
        finds the maximum area of a square that can fit inside the intersection
        region of at least two rectangles. Returns 0 if no such square exists.

        Each rectangle is defined by its bottom-left and top-right coordinates.
        bottomLeft[i] = [a_i, b_i], topRight[i] = [c_i, d_i] represent the
        coordinates of the ith rectangle.

        Args:
            bottomLeft (List[List[int]]): List of [x, y] for the bottom-left of each rectangle.
            topRight (List[List[int]]): List of [x, y] for the top-right of each rectangle.

        Returns:
            int: The maximum area of a square that can fit in the intersection
            of at least two rectangles. Returns 0 if no such square exists.

        Example:
            Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
            Output: 1

        Time Complexity: O(n^2), where n is the number of rectangles.
        Space Complexity: O(1), not including input.

        LeetCode: Beats 94.81% of submissions
        """
        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                left = max(x1, x3)
                right = min(x2, x4)
                bottom = max(y1, y3)
                top = min(y2, y4)

                if left < right and bottom < top:
                    side = min(right - left, top - bottom)
                    ans = max(ans, side * side)

        return ans
