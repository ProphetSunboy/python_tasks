class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
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
