class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        """Finds the maximum number of words in any sentence from a list of sentences.

        A sentence is a list of words separated by a single space with no leading or trailing spaces.

        Args:
            sentences (list[str]): A list of sentences where each sentence is a string

        Returns:
            int: The maximum number of words found in any single sentence

        Example:
            >>> mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
            6  # "this is great thanks very much" has the most words

        Time complexity: O(n * m) - where n is number of sentences and m is length of longest sentence
        Space complexity: O(1) - constant space used

        LeetCode: Beats 100% of submissions
        """
        max_words = 0

        for sentence in sentences:
            if len(sentence.split()) > max_words:
                max_words = len(sentence.split())

        return max_words
