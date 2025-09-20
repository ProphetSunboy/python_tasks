class Solution:
    def minimumMoves(self, s: str) -> int:
        """
        Given a string s consisting of 'X' and 'O' characters, return the minimum
        number of moves required to convert all characters to 'O'.

        A move consists of selecting any three consecutive characters and converting them all to 'O'.
        Characters that are already 'O' remain unchanged.

        Args:
            s (str): The input string of length n.

        Returns:
            int: The minimum number of moves needed to convert all characters to 'O'.

        Example:
            >>> minimumMoves("XXOX")
            2

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i = 0
        moves = 0

        while i < len(s):
            if s[i] == "X":
                i += 3
                moves += 1
            else:
                i += 1

        return moves
