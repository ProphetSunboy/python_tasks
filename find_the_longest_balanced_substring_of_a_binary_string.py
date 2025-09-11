class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        """
        Finds the length of the longest balanced substring in a binary string.

        A balanced substring is defined as a contiguous sequence where all
        zeroes ('0') come before all ones ('1'), and the number of zeroes is equal
        to the number of ones.

        Args:
            s (str): The input binary string consisting only of '0's and '1's.

        Returns:
            int: The length of the longest balanced substring.

        Example:
            >>> findTheLongestBalancedSubstring("01000111")
            6
            >>> findTheLongestBalancedSubstring("00111")
            4
            >>> findTheLongestBalancedSubstring("111")
            0

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        last, longest = 0, 0
        z, o = 0, 0

        for num in s:
            if num == "0":
                if last == "0":
                    z += 1
                else:
                    min_bin = min(z, o)
                    if min_bin * 2 > longest:
                        longest = min_bin * 2

                    z = 1
                    o = 0
                    last = "0"
            else:
                last = "1"
                o += 1
                min_bin = min(z, o)
                if min_bin * 2 > longest:
                    longest = min_bin * 2

        min_bin = min(z, o)
        if min_bin * 2 > longest:
            longest = min_bin * 2

        return longest
