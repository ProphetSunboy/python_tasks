class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        """Returns the number of strings that appear exactly once in both input
        string lists `words1` and `words2`.

        A string is counted if it occurs exactly once in `words1` and exactly once in `words2`.

        Args:
            words1 (List[str]): First list of lowercase English strings.
            words2 (List[str]): Second list of lowercase English strings.

        Returns:
            int: The number of strings that appear exactly once in each of the two lists.

        Example:
            >>> countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"])
            2
            # "leetcode" and "amazing" each appear exactly once in both lists.

        Time complexity: O(n + m), where n and m are the lengths of words1 and words2, respectively.
        Space complexity: O(n + m).

        LeetCode: Beats 100% of submissions
        """
        c1 = Counter(words1)
        c2 = Counter(words2)
        counter = 0

        for word, freq in c1.items():
            if freq == 1 and c2.get(word, 0) == 1:
                counter += 1

        return counter
