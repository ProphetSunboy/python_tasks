class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        """
        Given a 2D list `points` of size n x 2 representing integer coordinates on a 2D plane (points[i] = [xi, yi]),
        count the number of ordered pairs of points (A, B) such that:
            - A is on the upper left side of B (i.e., x_A <= x_B and y_A >= y_B),
            - There are no other points (including on the border) inside the rectangle defined by A and B.

        Args:
            points (list[list[int]]): List of [x, y] coordinates.

        Returns:
            int: The number of valid (A, B) pairs.

        Example:
            >>> numberOfPairs([[6,2],[4,4],[2,6]])
            2

        Time Complexity: O(n^3), where n is the number of points.
        Space Complexity: O(1), not counting input storage.
        """
        n = len(points)
        count = 0

        for i in range(n):
            x_a, y_a = points[i]
            for j in range(n):
                if i == j:
                    continue
                x_b, y_b = points[j]

                if x_a <= x_b and y_a >= y_b:
                    empty = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x_k, y_k = points[k]
                        if x_a <= x_k <= x_b and y_b <= y_k <= y_a:
                            empty = False
                            break

                    if empty:
                        count += 1

        return count
