class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        Return the reformatted license key.

        You are given a license key represented as a string s that consists of
        only alphanumeric characters and dashes. The string is separated into
        n + 1 groups by n dashes. You are also given an integer k.

        We want to reformat the string s such that each group contains exactly k
        characters, except for the first group, which could be shorter than k
        but still must contain at least one character. Furthermore, there must
        be a dash inserted between two groups, and you should convert all
        lowercase letters to uppercase.


        :param str s: original license key
        :param int k: size of group
        :returns str key: reformatted license key

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.50%
        """
        res = []
        key = s.replace("-", "").upper()

        if len(key) % k == 0:
            res.append(key[:k])
        else:
            res.append(key[: len(key) % k])

        for i in range(len(res[0]), len(key), k):
            res.append(key[i : i + k])

        return "-".join(res)
