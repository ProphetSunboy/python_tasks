class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        """Given two 0-indexed strings s and target, return the maximum number of
        copies of target that can be formed by taking letters from s and rearranging them.

        Each letter in s can be used at most once per copy. The order of letters in s does not matter.

        Args:
            s (str): The source string from which letters can be taken.
            target (str): The target string to form.

        Returns:
            int: The maximum number of copies of target that can be formed from s.

        Example:
            >>> rearrangeCharacters("ilovecodingonleetcode", "code")
            2

        Time complexity: O(n + m), where n = len(s), m = len(target)
        Space complexity: O(1) (since the alphabet size is constant)

        LeetCode: Beats 100% of submissions
        """
        c = Counter(s)
        c_t = Counter(target)

        max_copies = c[target[0]] // c_t[target[0]]
        for ch, freq in c_t.items():
            if c[ch] // freq < max_copies:
                max_copies = c[ch] // freq

        return max_copies
