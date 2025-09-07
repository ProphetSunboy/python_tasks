class Solution:
    def minLength(self, s: str) -> int:
        """
        Given a string s consisting only of uppercase English letters, repeatedly
        remove any occurrence of the substrings "AB" or "CD" from s in any order.
        After each removal, the string concatenates and may form new "AB" or "CD" substrings.

        Return the minimum possible length of the resulting string after performing any number of such operations.

        Args:
            s (str): The input string consisting of uppercase English letters.

        Returns:
            int: The minimum possible length of the string after all possible removals.

        Example:
            >>> minLength("ABFCACDB")
            2

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
                continue

            if ch == "B" and stack[-1] == "A":
                stack.pop()
            elif ch == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)
