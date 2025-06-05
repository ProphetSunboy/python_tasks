class Solution:
    def sortSentence(self, s: str) -> str:
        """Reconstructs the original sentence from a shuffled version where each word has its position appended.

        A sentence is a list of words separated by single spaces with no leading/trailing spaces.
        Each word consists of lowercase and uppercase English letters.

        The input sentence is shuffled by appending the 1-indexed position to each word.
        For example: "This is a sentence" becomes "sentence4 a3 is2 This1"

        Args:
            s (str): Shuffled sentence

        Returns:
            str: The original sentence

        Example:
            >>> sortSentence("sentence4 a3 is2 This1")
            "This is a sentence"

        Time complexity: O(n) - single pass through words to reconstruct
        Space complexity: O(n) - stores words in list for reconstruction


        LeetCode: Beats 98.09% of submissions
        """
        words = s.split()
        original = [""] * len(words)

        for word in words:
            original[int(word[-1]) - 1] = word[:-1]

        return " ".join(original)
