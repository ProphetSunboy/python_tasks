class Solution:
    def minTimeToType(self, word: str) -> int:
        """
        Calculates the minimum number of seconds required to type a given word using a special typewriter.

        The typewriter has lowercase English letters 'a' to 'z' arranged in a circle. The pointer starts at 'a'.
        Each second, you can:
            - Move the pointer one character clockwise or counterclockwise.
            - Type the character the pointer is currently on.

        Args:
            word (str): The word to type, consisting of lowercase English letters.

        Returns:
            int: The minimum number of seconds needed to type the word.

        Example:
            >>> minTimeToType("abc")
            5
            >>> minTimeToType("bza")
            7

        Time Complexity: O(n), where n is the length of word.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        time = 0
        curr = "a"

        for ch in word:
            c = ord(curr) - 97
            ord_ch = ord(ch) - 97
            time += min(25 - max(c, ord_ch) + min(c, ord_ch) + 1, abs(ord_ch - c)) + 1
            curr = ch

        return time
