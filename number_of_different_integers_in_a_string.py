class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        """Counts the number of distinct integers in a string after replacing all non-digit characters with spaces.

        Given a string `word` consisting of digits and lowercase English letters,
        this function replaces every non-digit character with a space, splits the
        resulting string into substrings of digits, and counts how many unique
        integers (ignoring leading zeros) are present.

        Two integers are considered different if their decimal representations without leading zeros are different.

        Args:
            word (str): The input string containing digits and lowercase English letters.

        Returns:
            int: The number of distinct integers found in the string.

        Example:
            >>> numDifferentIntegers("a123bc34d8ef34")
            3
            # Explanation: The integers are "123", "34", and "8". "34" appears twice but is only counted once.

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(k), where k is the number of unique integers found.

        LeetCode: Beats 100% of submissions
        """
        i = 0
        seen = set()

        while i < len(word):
            if word[i].isdigit():
                num = ""
                for j in range(i, len(word)):
                    if word[j].isdigit():
                        num += word[j]
                    else:
                        seen.add(int(num))
                        break
                seen.add(int(num))
                i = j

            i += 1

        return len(seen)
