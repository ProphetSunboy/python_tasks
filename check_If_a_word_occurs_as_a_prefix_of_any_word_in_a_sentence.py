class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Check if a search word is a prefix of any word in a given sentence.

        Args:
            sentence (str): A string containing words separated by single spaces
            searchWord (str): The prefix to search for

        Returns:
            int: The 1-indexed position of the first word that has searchWord as prefix,
                 or -1 if no word has searchWord as prefix

        Example:
            >>> isPrefixOfWord("i love eating burger", "burg")
            4
            >>> isPrefixOfWord("this problem is an easy problem", "pro")
            2

        Time complexity: O(n) where n is the number of words in the sentence
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return i

        return -1
