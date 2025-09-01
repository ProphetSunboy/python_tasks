class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        """
        Counts the number of substrings of a binary string s that satisfy the k-constraint.

        A substring satisfies the k-constraint if either:
            - The number of '0's in the substring is at most k, or
            - The number of '1's in the substring is at most k.

        Args:
            s (str): The input binary string.
            k (int): The maximum allowed count for either '0's or '1's in a valid substring.

        Returns:
            int: The number of substrings of s that satisfy the k-constraint.

        Example:
            >>> countKConstraintSubstrings("1001", 1)
            9

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        k_subs = 0
        i, j = 0, 0
        curr_o, curr_z = 0, 0

        while j < len(s):
            if s[j] == "1":
                curr_o += 1
            else:
                curr_z += 1

            if curr_o > k and curr_z > k:
                while curr_o > k and curr_z > k:
                    if s[i] == "1":
                        curr_o -= 1
                    else:
                        curr_z -= 1
                    i += 1

            k_subs += curr_o + curr_z

            j += 1

        return k_subs
