class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Given a 0-indexed string `blocks` of length n consisting of characters 'W' (white) and 'B' (black),
        and an integer k, return the minimum number of recoloring operations needed to obtain at least
        one substring of length k consisting entirely of black blocks ('B').

        In one operation, you can recolor a 'W' (white) block to a 'B' (black) block.

        Args:
            blocks (str): The string representation of blocks, consisting of 'W' and 'B'.
            k (int): The required number of consecutive black blocks.

        Returns:
            int: The minimum number of recoloring operations required.

        Example:
            >>> minimumRecolors("WBBWWBBWBW", 7)
            3
            >>> minimumRecolors("WBWBBBW", 2)
            0

        Time Complexity: O(n), where n is the length of blocks.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        n = len(blocks)
        white = blocks[:k].count("W")
        min_ops = white

        for i in range(k, n):
            if blocks[i - k] == "W":
                white -= 1
            if blocks[i] == "W":
                white += 1
            min_ops = min(min_ops, white)

        return min_ops
