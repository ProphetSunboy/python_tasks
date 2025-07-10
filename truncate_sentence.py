class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """Truncates a sentence to contain only the first k words.

        Given a sentence `s` (a string of words separated by single spaces, with no leading or trailing spaces)
        and an integer `k`, this function returns a new sentence containing only the first `k` words from `s`.

        Args:
            s (str): The input sentence.
            k (int): The number of words to keep.

        Returns:
            str: The truncated sentence containing only the first `k` words.

        Example:
            >>> truncateSentence("Hello world this is great", 3)
            'Hello world this'

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(n), due to splitting and joining the string.

        LeetCode: Beats 100% of submissions
        """
        return " ".join(s.split()[:k])
