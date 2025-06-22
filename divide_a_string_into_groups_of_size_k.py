class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        """Divides a string `s` into groups of size `k`.

        The string is partitioned into groups of `k` characters. If the last
        group does not have `k` characters, it is padded with the `fill`
        character to reach the desired length.

        Args:
            s (str): The input string to divide.
            k (int): The size of each group.
            fill (str): The character to use for padding.

        Returns:
            list[str]: A list of strings, where each string is a group.

        Example:
            Input: s = "abcdefgh", k = 3, fill = "x"
            Output: ["abc", "def", "ghx"]

        Time complexity: O(N), where N is the length of s.
        Space complexity: O(N), to store the resulting list of groups.

        LeetCode: Beats 100% of submissions
        """
        groups = []

        filled_s = s.ljust(len(s) if len(s) % k == 0 else (len(s) // k + 1) * k, fill)

        for i in range(0, len(filled_s), k):
            groups.append(filled_s[i : i + k])

        return groups
