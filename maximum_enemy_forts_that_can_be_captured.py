class Solution:
    def captureForts(self, forts: List[int]) -> int:
        """
        Calculates the maximum number of enemy forts that can be captured in one move.

        You are given a 0-indexed integer list `forts` of length n, where:
            - `forts[i] == -1` means the i-th position is empty (no fort),
            - `forts[i] == 0` means there is an enemy fort at the i-th position,
            - `forts[i] == 1` means your fort is at the i-th position.

        You can move your army from a position with your fort (`1`) to an empty
        position (`-1`), only traversing through enemy forts (`0`).
        For a move from index i to j, all positions between i and j (exclusive)
        ust be enemy forts, i.e., for all k with min(i, j) < k < max(i, j): forts[k] == 0.
        All enemy forts passed over are captured.

        Returns the maximum number of enemy forts that can be captured in a single valid move.
        If no move is possible, or you do not own any forts, returns 0.

        Args:
            forts (List[int]): List describing fort positions.

        Returns:
            int: Maximum number of enemy forts that can be captured in one move.

        Example:
            >>> captureForts([1, 0, 0, -1, 0, 1])
            2

        Time Complexity: O(n), where n is the size of forts.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        n = len(forts)
        max_capture = 0

        for i in range(n):
            if forts[i] == 1:
                flag = True
                right_capture = 0

                for j in range(i + 1, n):
                    if forts[j] == 0:
                        right_capture += 1
                    elif forts[j] == -1:
                        flag = False
                        break
                    else:
                        break
                if flag:
                    right_capture = 0

                left_capture = 0
                flag = True

                for j in range(i - 1, -1, -1):
                    if forts[j] == 0:
                        left_capture += 1
                    elif forts[j] == -1:
                        flag = False
                        break
                    else:
                        break
                if flag:
                    left_capture = 0
                max_capture = max(max_capture, right_capture, left_capture)

        return max_capture
