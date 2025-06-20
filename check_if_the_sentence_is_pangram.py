class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """Checks if a sentence is a pangram.

        A pangram is a sentence where every letter of the English alphabet appears at least once.
        Given a string `sentence` containing only lowercase English letters, returns True if
        `sentence` is a pangram, or False otherwise.

        Args:
            sentence (str): The input string to check.

        Returns:
            bool: True if the sentence is a pangram, False otherwise.

        Example:
            >>> checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
            True

        Time complexity: O(N), where N is the length of the sentence.
        Space complexity: O(1), for tracking the 26 letters.

        LeetCode: Beats 100% of submissions
        """
        alph = [False] * 26

        for ch in sentence:
            alph[ord(ch) - 97] = True

        return all(alph)
