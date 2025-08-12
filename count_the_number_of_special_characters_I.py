class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        Given a string `word`, a letter is called special if it appears in both lowercase and uppercase forms in `word`.

        Returns the number of special letters in `word`.

        Args:
            word (str): The input string.

        Returns:
            int: The count of special letters.

        Example:
            >>> numberOfSpecialChars("aAbBcC")
            3

        Time Complexity: O(N), where N is the length of the input string.
        Space Complexity: O(1), since the number of possible letters is constant (26).

        LeetCode: Beats 100% of submissions
        """
        letters = set(word)
        seen = set()

        for l in letters:
            if l.lower() not in seen:
                if l.isupper() and l.lower() in letters:
                    seen.add(l.lower())
                elif l.islower() and l.upper() in letters:
                    seen.add(l)

        return len(seen)
