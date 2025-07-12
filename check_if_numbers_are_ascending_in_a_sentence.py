class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        """Checks if all numbers in a sentence are strictly increasing from left to right.

        A sentence is a string of tokens separated by single spaces, where each token is either:
            - a positive integer (no leading zeros), or
            - a word of lowercase English letters.

        This function extracts all numbers from the sentence and verifies that each number is strictly greater than the previous one.

        Args:
            s (str): The input sentence containing words and numbers.

        Returns:
            bool: True if all numbers are strictly increasing, False otherwise.

        Example:
            >>> areNumbersAscending("a puppy has 2 eyes 4 legs")
            True
            >>> areNumbersAscending("hello 5 world 5")
            False

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(1), as only a constant amount of extra space is used.

        LeetCode: Beats 100% of submissions
        """
        prev = -1

        for token in s.split():
            if token[0].isdigit():
                num = int(token)

                if num > prev:
                    prev = num
                else:
                    return False

        return True
