import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Given a string s, rearrange the characters of s so that any two adjacent
        characters are not the same.

        Return any possible rearrangement of s or return "" if not possible.

        :param int s: original strig
        :returns str res: rearrangement of s

        Time complexity: O(n^2logn)
        Space complexity: O(n)
        """
        coll = collections.Counter(s).items()
        res = ""
        prev = ""

        while len(res) < len(s):
            coll = sorted(coll, key=lambda item: item[1], reverse=True)

            l = len(res)

            for i, (ch, val) in enumerate(coll):
                if ch != prev and val > 0:
                    res += ch
                    coll[i] = (ch, val - 1)
                    prev = ch
                    break

            if l == len(res):
                return ""

        return res
