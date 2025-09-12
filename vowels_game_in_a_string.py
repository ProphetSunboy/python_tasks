class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """
        Determines if Alice wins the vowels game played on a string.

        Alice and Bob take turns playing a game on string s, with Alice starting first:
        - Alice removes any non-empty substring containing an odd number of vowels
        - Bob removes any non-empty substring containing an even number of vowels
        - The first player who cannot make a move loses
        - Both players play optimally

        Args:
            s (str): The input string containing lowercase English letters.

        Returns:
            bool: True if Alice wins the game, False if Bob wins.

        Examples:
            >>> doesAliceWin("aeiou")
            True
            >>> doesAliceWin("bcdfg")
            False
            >>> doesAliceWin("hello")
            True

        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(1)
        """
        for ch in s:
            if ch in "aeiou":
                return True

        return False
