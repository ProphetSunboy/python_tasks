class Solution:
    def reorderSpaces(self, text: str) -> str:
        """Rearrange spaces in a string so there are an equal number of spaces between words.

        Given a string containing words separated by spaces, redistribute the spaces so that:
        1. There is an equal maximum number of spaces between each pair of adjacent words
        2. Any extra spaces that cannot be distributed evenly are placed at the end
        3. The returned string has the same length as the input

        Args:
            text (str): A string containing words separated by one or more spaces

        Returns:
            str: The string with spaces rearranged according to the rules

        Example:
            >>> reorderSpaces("  this   is  a sentence ")
            "this   is   a   sentence  "
            >>> reorderSpaces("  walks  udp package   into  bar a")
            "walks  udp  package  into  bar  a "

        Time complexity: O(n) where n is the length of the input string
        Space complexity: O(n) to store the split words

        LeetCode: Beats 100% of submissions
        """
        total_spaces = text.count(" ")
        words = text.split()
        spaces_between_words = 0
        extra_spaces = total_spaces

        if len(words) > 1:
            spaces_between_words = total_spaces // (len(words) - 1)
            extra_spaces = total_spaces % (len(words) - 1)

        return (" " * spaces_between_words).join(words) + " " * extra_spaces
