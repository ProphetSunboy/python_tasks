class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """
        Given a string list words, return a list of all characters that show up
        in all strings within the words (including duplicates).
        You may return the answer in any order.

        :param list[str] words: string list
        :returns list[str] res: all characters that show up in all strings
        within the words (including duplicates)

        Time complexity: O(n^2)
        Space complexity: O(n)

        LeetCode: Beats 98.39%
        """

        def find_common(first, second):
            s = collections.Counter(second)

            return {
                ch: min(freq, s[ch]) for ch, freq in first.items() if s.get(ch, 0) > 0
            }

        commons = find_common(collections.Counter(words[0]), words[1])
        for i in range(2, len(words)):
            commons = find_common(commons, words[i])

        res = []
        for ch, freq in commons.items():
            res += [ch] * freq

        return res
