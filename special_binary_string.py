class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        Returns the lexicographically largest special binary string possible by
        repeatedly swapping consecutive, non-empty special substrings.

        A special binary string is defined as a binary string satisfying:
            1. The number of '0's is equal to the number of '1's.
            2. Every prefix has at least as many '1's as '0's.

        A move consists of choosing two consecutive, non-empty, special substrings
        of s and swapping them.

        Args:
            s (str): A special binary string.

        Returns:
            str: The lexicographically largest special binary string obtainable.

        Example:
            Input: s = "11011000"
            Output: "11100100"

        Time Complexity: O(n^2), due to recursive splitting and sorting of up
        to O(n) substrings, each at most O(n) to process.
        Space Complexity: O(n^2), from recursion stack and storage of substrings.

        LeetCode: Beats 100% of submissions
        """
        count = 0
        i = 0
        res = []

        for j, char in enumerate(s):
            count += 1 if char == "1" else -1

            if count == 0:
                inner_part = self.makeLargestSpecial(s[i + 1 : j])
                res.append("1" + inner_part + "0")

                i = j + 1

        return "".join(sorted(res, reverse=True))
