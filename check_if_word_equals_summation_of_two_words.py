class Solution:
    def summation(self, s: str) -> int:
        """Converts a string of lowercase English letters ('a'-'j') into its numerical value
        by concatenating the letter values (where 'a' = 0, 'b' = 1, ..., 'j' = 9) and converting the result to an integer.

        Args:
            s (str): A string consisting of lowercase English letters from 'a' to 'j'.

        Returns:
            int: The integer value formed by concatenating the letter values of the input string.

        Example:
            >>> summation("acb")
            21  # 'a'->0, 'c'->2, 'b'->1, so "021" -> 21
        """
        res = ""
        for ch in s:
            res += str(ord(ch) - 97)

        return int(res)

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """Determines if the sum of the numerical values of two words equals the numerical value of a target word.

        The letter value of a character is its position in the alphabet starting from 0 (i.e., 'a' -> 0, 'b' -> 1, ..., 'j' -> 9).
        The numerical value of a string is formed by concatenating the letter values of each character and converting the result to an integer.

        For example:
            If s = "acb", then the letter values are 'a' = 0, 'c' = 2, 'b' = 1, so the concatenated string is "021", which converts to 21.

        Args:
            firstWord (str): The first input word, consisting of lowercase English letters 'a' to 'j'.
            secondWord (str): The second input word, consisting of lowercase English letters 'a' to 'j'.
            targetWord (str): The target word, consisting of lowercase English letters 'a' to 'j'.

        Returns:
            bool: True if the sum of the numerical values of firstWord and secondWord equals the numerical value of targetWord, False otherwise.

        Example:
            >>> isSumEqual("acb", "cba", "cdb")
            True

        Time complexity: O(n), where n is the total number of characters in all input strings.
        Space complexity: O(1), excluding input and output.

        LeetCode: Beats 100% of submissions
        """
        return self.summation(firstWord) + self.summation(secondWord) == self.summation(
            targetWord
        )
