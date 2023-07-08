class Solution:
    def similarPairs(self, words: list[str]) -> int:
        """
        You are given a 0-indexed string array words.

        Two strings are similar if they consist of the same characters.

        For example, "abca" and "cba" are similar since both consist of
        characters 'a', 'b', and 'c'.
        However, "abacba" and "bcfd" are not similar since they do not consist
        of the same characters.

        Return the number of pairs (i, j) such that
        0 <= i < j <= word.length - 1 and the two strings words[i] and words[j]
        are similar.

        LeetCode: Beats 96.1%
        """
        counter = 0
        pairs = {}

        for word in words:
            w = tuple(sorted(set(word)))

            if w not in pairs:
                pairs[w] = 1
            else:
                counter += pairs[w]
                pairs[w] += 1

        return counter