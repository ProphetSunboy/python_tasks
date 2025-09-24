class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        For a string `sequence`, a string `word` is k-repeating if `word` concatenated k times is a substring of `sequence`.
        The maximum k-repeating value is the largest integer k such that `word * k` is a substring of `sequence`.
        If `word` is not a substring of `sequence`, the maximum k-repeating value is 0.

        Given strings `sequence` and `word`, return the maximum k-repeating value of `word` in `sequence`.

        Args:
            sequence (str): The string in which to search for repeated substrings.
            word (str): The substring to repeat and search for.

        Returns:
            int: The maximum value k such that `word * k` is a substring of `sequence`.

        Example:
            >>> maxRepeating("ababc", "ab")
            2
            >>> maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba")
            5
            >>> maxRepeating("baba", "b")
            1

        Time Complexity: O(N * K), where N is the length of `sequence` and K is the maximum possible k.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        max_k_val = 0
        i = 0

        curr_k_val = 0
        while i < len(sequence):
            if sequence[i : i + len(word)] == word:
                curr_k_val += 1
                i += len(word)
            else:
                if curr_k_val > max_k_val:
                    max_k_val = curr_k_val

                if curr_k_val > 0:
                    curr_k_val = 0
                    i -= len(word)

                i += 1

        if curr_k_val > max_k_val:
            max_k_val = curr_k_val

        return max_k_val
