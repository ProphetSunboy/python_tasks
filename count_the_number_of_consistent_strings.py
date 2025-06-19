class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """Counts the number of consistent strings in the given list.

        A string is considered consistent if every character in the string appears in the string `allowed`.

        Args:
            allowed (str): A string of distinct allowed characters.
            words (list[str]): List of words to check for consistency.

        Returns:
            int: The number of consistent strings in `words`.

        Examples:
            >>> countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])
            2
            >>> countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"])
            4

        Time complexity: O(N * M), where N is the number of words and M is the average length of a word.
        Space complexity: O(1), ignoring input and output storage.

        LeetCode: Beats 97.21% of submissions
        """
        consistent_strings = 0

        for word in words:
            word_consistent = True

            for ch in word:
                if ch not in allowed:
                    word_consistent = False
                    break

            consistent_strings += word_consistent

        return consistent_strings
