class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """
        Given a list of strings `words`, determine if it is possible to make all
        strings equal by repeatedly moving any character from one string to any
        position in another string.

        In each operation, you may pick two distinct indices i and j (where words[i] is non-empty)
        and move any character from words[i] to any position in words[j].

        Args:
            words (List[str]): List of input strings.

        Returns:
            bool: True if all strings can be made equal using any number of operations, False otherwise.

        Example:
            >>> makeEqual(["abc", "aabc", "bc"])
            True

        Time Complexity: O(N), where N is the total number of characters in all strings.
        Space Complexity: O(1) (since the alphabet size is constant).

        LeetCode: Beats 98.09% of submissions
        """
        words_join = "".join(words)
        lengths = len(words_join)

        if lengths % len(words):
            return False

        letters = Counter(words_join)

        for freq in letters.values():
            if freq % len(words):
                return False

        return True
