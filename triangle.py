class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Given a triangle list, return the minimum path sum from top to bottom.

        At each step, you may move to an adjacent number in the row below.
        More formally, if you are at index i in the current row, you may move to
        index i or i + 1 in the next row.

        Args:
            triangle (List[List[int]]): The triangle represented as a list of lists of integers.

        Returns:
            int: The minimum path sum from top to bottom.

        Example:
            >>> minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
            11
            # Explanation: 2 + 3 + 5 + 1 = 11

        Time Complexity: O(N^2), where N is the number of rows in the triangle.
        Space Complexity: O(N^2), for the DP table.

        LeetCode: Beats 100% of submissions
        """
        paths = [[triangle[0][0]]]

        for i in range(1, len(triangle)):
            paths.append([0] * (i + 1))

            for j in range(i + 1):
                if j == 0:
                    paths[i][j] = triangle[i][j] + paths[i - 1][j]
                elif j == i:
                    paths[i][j] = triangle[i][j] + paths[i - 1][j - 1]
                else:
                    paths[i][j] = triangle[i][j] + min(
                        paths[i - 1][j], paths[i - 1][j - 1]
                    )

        return min(paths[-1])
