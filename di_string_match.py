class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        """
        A permutation perm of n + 1 integers of all the integers in the range
        [0, n] can be represented as a string s of length n where:

            s[i] == 'I' if perm[i] < perm[i + 1], and
            s[i] == 'D' if perm[i] > perm[i + 1].

        Given a string s, reconstruct the permutation perm and return it. If
        there are multiple valid permutations perm, return any of them.

        :param str s: list of integers
        :returns list[int] res: nums is a valid mountain list

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.12%
        """
        vals = {"I": 0, "D": -len(s)}
        perm = [0] * (len(s) + 1)

        for k in range(len(s)):
            perm[k] = abs(vals[s[k]])
            vals[s[k]] += 1

        perm[-1] = vals["I"]

        return perm
