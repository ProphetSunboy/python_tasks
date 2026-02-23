class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Return True if every binary code of length k is a substring of the
        given binary string s.

        Args:
            s (str): A binary string to search within.
            k (int): The length of the binary codes to check for.

        Returns:
            bool: True if every binary code of length k is a substring of s,
            otherwise False.

        Example:
            Input:
                s = "00110110"
                k = 2
            Output:
                True

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(2^k), for tracking seen binary codes of length k.

        LeetCode: Beats 96.00% of submissions
        """
        required_count = 1 << k
        seen = [False] * required_count
        count = 0

        mask = required_count - 1

        current_hash = 0
        for i in range(len(s)):
            current_hash = ((current_hash << 1) & mask) | int(s[i])

            if i >= k - 1:
                if not seen[current_hash]:
                    seen[current_hash] = True
                    count += 1
                    if count == required_count:
                        return True

        return False
