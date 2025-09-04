class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        """
        Flips a k x k square submatrix of grid vertically (reverses the order of its rows).

        Args:
            grid (List[List[int]]): The m x n integer matrix.
            x (int): Row index of the top-left corner of the submatrix.
            y (int): Column index of the top-left corner of the submatrix.
            k (int): Size (side length) of the square submatrix.

        Returns:
            List[List[int]]: The updated matrix after flipping the submatrix vertically.

        Example:
            >>> grid = [
            ...     [1, 2, 3, 4],
            ...     [5, 6, 7, 8],
            ...     [9,10,11,12],
            ...     [13,14,15,16]
            ... ]
            >>> reverseSubmatrix(grid, 1, 1, 2)
            [
                [1, 2, 3, 4],
                [5,10,11,8],
                [9, 6, 7,12],
                [13,14,15,16]
            ]

        Time Complexity: O(k^2)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for j in range(y, y + k):
            for i in range(x, x + k):
                if i >= x + k // 2:
                    break
                grid[i][j], grid[x + k - (i - x) - 1][j] = (
                    grid[x + k - (i - x) - 1][j],
                    grid[i][j],
                )

        return grid
