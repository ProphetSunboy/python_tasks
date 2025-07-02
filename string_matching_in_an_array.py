class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """Given a list of strings `words`, return all strings in `words` that are a substring of another word in the list.
        The answer can be returned in any order.

        Args:
            words (list[str]): The list of strings to check.

        Returns:
            list[str]: A list of strings from `words` that are substrings of another word in the list.

        Example:
            >>> stringMatching(["mass","as","hero","superhero"])
            ['as', 'hero']
            >>> stringMatching(["leetcode","et","code"])
            ['et', 'code']
            >>> stringMatching(["blue","green","bu"])
            []

        LeetCode: Beats 100% of submissions
        """
        words.sort(key=len)
        res = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break

        return res
