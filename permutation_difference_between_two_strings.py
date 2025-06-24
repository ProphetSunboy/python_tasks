class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        """Calculates the permutation difference between two strings.

        Given two strings, `s` and `t`, where `t` is a permutation of `s`,
        the permutation difference is the sum of the absolute differences
        between the indices of each character in `s` and `t`.

        Args:
            s (str): The first string.
            t (str): The second string, a permutation of `s`.

        Returns:
            int: The total permutation difference.

        Example:
            Input: s = "abc", t = "bac"
            Output: 2
            Explanation:
            'a' is at index 0 in s and 1 in t, difference is 1.
            'b' is at index 1 in s and 0 in t, difference is 1.
            'c' is at index 2 in s and 2 in t, difference is 0.
            Total difference = 1 + 1 + 0 = 2.

        LeetCode: Beats 100% of submissions
        """
        perm_diff = 0
        s_occ = dict()
        t_occ = dict()

        for i, (s_ch, t_ch) in enumerate(zip(s, t)):
            s_occ[s_ch] = i
            t_occ[t_ch] = i

        for key, val in s_occ.items():
            perm_diff += abs(val - t_occ[key])

        return perm_diff
