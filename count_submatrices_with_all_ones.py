class Solution:
    def numSubmat(self, matrix: list[list[int]]) -> int:
        """
        Counts the number of submatrices with all ones in a given m x n binary matrix.

        Args:
            matrix (list[list[int]]): 2D binary matrix (list of lists) of size m x n.

        Returns:
            int: The total number of submatrices that contain only ones.

        Example:
            >>> numSubmat([[1,0,1],[1,1,0],[1,1,0]])
            13

        Time Complexity: O(m * n^2)
        Space Complexity: O(1)
        """
        submat = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    submat += 1
                    k = j + 1
                    if k == len(matrix[0]) or matrix[i][k] == 0:
                        k -= 1

                    while k < len(matrix[0]) - 1 and matrix[i][k] == 1:
                        k += 1

                    if matrix[i][k] == 0:
                        k -= 1

                    min_depth = 1
                    for h in range(i + 1, len(matrix)):
                        if matrix[h][j] == 1:
                            min_depth += 1
                            submat += 1
                        else:
                            break

                    for l in range(j + 1, k + 1):
                        submat += 1
                        curr_depth = 1
                        for h in range(i + 1, len(matrix)):
                            if matrix[h][l] == 0:
                                if curr_depth < min_depth:
                                    min_depth = curr_depth
                                break

                            curr_depth += 1

                            if min_depth == 1:
                                break
                            if curr_depth <= min_depth:
                                submat += 1
                            else:
                                break

        return submat
