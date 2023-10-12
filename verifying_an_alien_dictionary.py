class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        """
        In an alien language, surprisingly, they also use English lowercase
        letters, but possibly in a different order. The order of the alphabet is
        some permutation of lowercase letters.

        Given a sequence of words written in the alien language, and the order
        of the alphabet, return True if and only if the given words are sorted
        lexicographically in this alien language.

        :param list[str] words: sequence of lowercase words
        :param str order: order of the alien alphabet
        :returns bool lexicograph: words are sorted lexicographically in alien
        language

        Time complexity: O(n^2)
        Space complexity: O(1)

        LeetCode: Beats 93.81%
        """
        vocab = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            lexicograph = False
            for a, b in zip(words[i], words[i + 1]):
                if vocab[a] == vocab[b]:
                    continue
                else:
                    if vocab[a] > vocab[b]:
                        return False
                    else:
                        lexicograph = True
                        break

            if not lexicograph and len(words[i]) > len(words[i + 1]):
                return False

        return True
