class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        """Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

        Args:
            words (List[str]): List of lowercase English strings.
            s (str): The target string to check prefixes against.

        Returns:
            int: The number of strings in `words` that are prefixes of `s`.

        Example:
            >>> countPrefixes(["a", "b", "ab", "abc"], "abc")
            3
            # "a", "ab", and "abc" are prefixes of "abc".

        Time complexity: O(n * m), where n is the number of words and m is the average length of the words.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        c1 = Counter(words1)
        c2 = Counter(words2)
        counter = 0

        for word, freq in c1.items():
            if freq == 1 and c2.get(word, 0) == 1:
                counter += 1

        return counter
