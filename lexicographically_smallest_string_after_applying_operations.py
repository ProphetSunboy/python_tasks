class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        Given a string s of even length consisting of digits ('0'-'9'), and two integers a and b,
        perform the following operations any number of times in any order to obtain the lexicographically smallest string:

        1. Add 'a' to all digits at odd indices (0-based). Digits wrap around from '9' to '0' as needed.
           Example: If s = "3456" and a = 5, s becomes "3951".
        2. Rotate the string to the right by 'b' positions.
           Example: If s = "3456" and b = 1, s becomes "6345".

        Return the lexicographically smallest string achievable.

        Lexicographical order means string a is smaller than b if at the first differing character,
        a has a digit smaller than b. Example: "0158" < "0190".

        Args:
            s (str): The original numeric string of even length.
            a (int): The value to add to odd indices.
            b (int): The rotation amount.

        Returns:
            str: Lexicographically smallest string possible after operations.

        Example:
            >>> findLexSmallestString("5525", 9, 2)
            "2050"

        Time Complexity: O(N^2), where N = len(s)
        Space Complexity: O(N^2)

        LeetCode: Beats 90.65% of submissions
        """
        n = len(s)

        s = list(map(int, s))

        def add_to_odd_positions(s, a):
            for i in range(1, len(s), 2):
                s[i] = (s[i] + a) % 10
            return s

        def rotate_right(s, b):
            b = b % n
            return s[-b:] + s[:-b]

        seen = set()
        min_string = s[:]
        queue = [s]

        while queue:
            current_s = queue.pop(0)

            min_string = min(min_string, current_s)

            rotated_s = rotate_right(current_s, b)
            if tuple(rotated_s) not in seen:
                seen.add(tuple(rotated_s))
                queue.append(rotated_s)

            modified_s = add_to_odd_positions(current_s[:], a)
            if tuple(modified_s) not in seen:
                seen.add(tuple(modified_s))
                queue.append(modified_s)

        return "".join(map(str, min_string))
