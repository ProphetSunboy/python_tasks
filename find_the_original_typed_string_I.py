class Solution:
    def possibleStringCount(self, word: str) -> int:
        """Given a string `word` representing the final output typed by Alice,
        who may have accidentally held down a key and repeated a character at
        most once, return the total number of possible original strings Alice
        could have intended to type.

        Alice may have typed the intended string perfectly, or she may have
        accidentally repeated a single character (i.e., one group of consecutive
        identical characters could be the result of a single extra keypress).

        Args:
            word (str): The string as displayed on Alice's screen.

        Returns:
            int: The number of possible original strings Alice could have intended.

        Example:
            >>> possibleStringCount("aabb")
            3
            >>> possibleStringCount("abc")
            1
            >>> possibleStringCount("aabbc")
            3

        LeetCode: Beats 100% of submissions
        """
        possible_s = 1

        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                possible_s += 1

        return possible_s
