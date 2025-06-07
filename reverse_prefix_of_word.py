# First attempt
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = word

        for i, l in enumerate(word):
            if l == ch:
                res = word[i::-1] + word[i + 1 :]
                break

        return res


# Second attempt
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """Reverses the prefix of a string up to and including the first occurrence of a character.

        Given a 0-indexed string word and a character ch, reverses the segment of word that starts
        at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character
        ch does not exist in word, returns the original string unchanged.

        Args:
            word (str): The input string to process
            ch (str): The character to search for

        Returns:
            str: The string with the prefix reversed up to ch, or the original string if ch not found

        Example:
            >>> reversePrefix("abcdefd", "d")
            'dcbaefd'

        Time complexity: O(n) - where n is the length of the string
        Space complexity: O(n) - for storing the result string
        """
        res = word

        idx = word.find(ch)

        if idx > -1:
            res = word[idx::-1] + word[idx + 1 :]

        return res
