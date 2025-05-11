# First Solution
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        """
        Given a list of dominoes, dominoes[i] = [a, b] is equivalent to
        dominoes[j] = [c, d] if and only if either (a == c and b == d), or
        (a == d and b == c) - that is, one domino can be rotated to be equal to
        another domino.

        Return the number of pairs (i, j) for which 0 <= i < j <
        dominoes.length, and dominoes[i] is equivalent to dominoes[j].
        """
        seen = dict()
        s = 0

        for d in dominoes:
            k = tuple(d)
            if seen.get(k):
                seen[k] += 1
            elif seen.get((d[1], d[0])):
                seen[(d[1], d[0])] += 1
            else:
                seen[k] = 1

        for v in seen.values():
            if v > 1:
                s += (v * (v + 1)) // 2 - v

        return s


# Second Solution
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        seen = []
        s = 0

        for d in dominoes:
            if d not in seen:
                k = dominoes.count(d) - 1

                if d[0] != d[1]:
                    k += dominoes.count([d[1], d[0]])

                s += (k * (k + 1)) // 2

                seen.append(d)
                seen.append([d[1], d[0]])

        return s
