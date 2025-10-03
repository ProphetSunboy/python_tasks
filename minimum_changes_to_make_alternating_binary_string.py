class Solution:
    def minOperations(self, s: str) -> int:
        """
        Given a binary string s, returns the minimum number of operations required to make s alternating.

        An alternating string is one in which no two adjacent characters are the same (e.g., "0101" or "1010").
        In one operation, you can change any '0' to '1' or vice versa.

        Args:
            s (str): A binary string consisting only of '0' and '1'.

        Returns:
            int: The minimum number of changes needed to make s alternating.

        Example:
            >>> minOperations("0100")
            1
            >>> minOperations("10")
            0

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 99.38% of submissions
        """
        start = ["0", "1"]
        changes = 0

        for ch in start:
            curr = ch
            curr_changes = 0
            for n in s:
                if n != curr:
                    curr_changes += 1

                if curr == "0":
                    curr = "1"
                else:
                    curr = "0"

            if ch == "0":
                changes = curr_changes

        return min(changes, curr_changes)
