class Solution:
    def countValidWords(self, sentence: str) -> int:
        """Counts the number of valid words in a given sentence.

        A sentence consists of lowercase letters ('a'-'z'), digits ('0'-'9'),
        hyphens ('-'), punctuation marks ('!', '.', ','), and spaces (' ').
        The sentence is split into tokens by one or more spaces.

        A token is considered a valid word if all of the following are true:
            1. It contains only lowercase letters, hyphens, and/or punctuation marks (no digits).
            2. It contains at most one hyphen ('-'), which must be surrounded by
            lowercase letters (e.g., "a-b" is valid, but "-ab" and "ab-" are not).
            3. It contains at most one punctuation mark ('!', '.', ','), which must
            appear at the end of the token (e.g., "ab,", "cd!", and "." are valid, but "a!b" and "c.," are not).

        Args:
            sentence (str): The input sentence to evaluate.

        Returns:
            int: The number of valid words in the sentence.

        Example:
            >>> countValidWords("a-b.")
            True
            >>> countValidWords(".ac")
            False

        Time complexity: O(n), where n is the length of the sentence.
        Space complexity: O(k), where k is the number of tokens.

        LeetCode: Beats 100% of submissions
        """
        tokens = sentence.split()
        valid_words = 0

        for token in tokens:
            hephens = 0
            valid = True
            for i, ch in enumerate(token):
                if ch.isalpha():
                    continue
                elif ch.isdigit():
                    valid = False
                    break
                elif ch == "-":
                    hephens += 1
                    if hephens > 1:
                        valid = False
                        break
                    if i == 0 or i == len(token) - 1:
                        valid = False
                        break
                    elif not token[i - 1].isalpha() or not token[i + 1].isalpha():
                        valid = False
                        break
                elif i != len(token) - 1:
                    valid = False
                    break

            valid_words += valid

        return valid_words
