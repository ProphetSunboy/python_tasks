class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        """
        Returns the words that can be typed using letters from only one row of an American keyboard.

        Each word in the input list is checked to see if all its letters (case-insensitive) are contained within a single keyboard row:
            - First row: "qwertyuiop"
            - Second row: "asdfghjkl"
            - Third row: "zxcvbnm"

        Args:
            words (List[str]): The input list of words.

        Returns:
            List[str]: A list of words that can be typed using one keyboard row.

        Example:
            >>> findWords(["Hello", "Alaska", "Dad", "Peace"])
            ['Alaska', 'Dad']

        Time Complexity: O(N * M), where N is the number of words and M is the average length of a word.
        Space Complexity: O(1) (excluding the output list).

        LeetCode: Beats 100% of submissions
        """
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        one_row = []

        for word in words:
            letters = set(word.lower())
            for row in rows:
                if letters.intersection(row) == letters:
                    one_row.append(word)
                    break

        return one_row
