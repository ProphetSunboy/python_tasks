class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Given a rows x cols binary matrix filled with '0's and '1's,
        find the largest rectangle containing only '1's and return its area.

        Args:
            matrix (List[List[str]]): Binary matrix represented as a list of lists,
                where each element is either '0' or '1'.

        Returns:
            int: The area of the largest rectangle containing only '1's.

        Example:
            Input:
                matrix = [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"]
                ]
            Output:
                6

        Time Complexity: O(m * n), where m is the number of rows and n is the
        number of columns.
        Space Complexity: O(n), where n is the number of columns
        (for the heights list).

        LeetCode: Beats 99.87% of submissions
        """
        n = len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0

        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
