import numpy as np


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Determines if the matrix `mat` can be rotated in 90-degree increments
        (clockwise) to match the matrix `target`.

        Args:
            mat (List[List[int]]): The original n x n binary matrix.
            target (List[List[int]]): The target n x n binary matrix.

        Returns:
            bool: True if `mat` can be rotated (0, 90, 180, or 270 degrees) to equal `target`, False otherwise.

        Example:
            >>> findRotation([[0,1],[1,0]], [[1,0],[0,1]])
            True
            >>> findRotation([[0,1],[1,1]], [[1,0],[0,1]])
            False

        Time Complexity: O(n^2), where n is the size of the matrix.
        Space Complexity: O(n^2), due to matrix copying during rotation.

        LeetCode: Beats 100% of submissions
        """
        if mat == target:
            return True
        for i in range(-3, 0):
            if np.rot90(mat, k=i).tolist() == target:
                return True

        return False
