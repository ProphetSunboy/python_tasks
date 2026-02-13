class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Given a string s consisting only of the characters 'a', 'b', and 'c',
        return the length of the longest balanced substring.

        A substring is called balanced if all distinct characters in the
        substring appear the same number of times.

        Args:
            s (str): The input string consisting of 'a', 'b', and 'c' only.

        Returns:
            int: The length of the longest balanced substring.

        Example:
            Input: s = 'abacbc'
            Output: 6

        Time Complexity: O(n), since we iterate over the string once.
        Space Complexity: O(n), since we use a dictionary to store the lookup.

        LeetCode: Beats 99.27% of submissions
        """
        n = len(s)
        if n == 0:
            return 0
        max_l = 0

        curr_len = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                curr_len += 1
            else:
                if curr_len > max_l:
                    max_l = curr_len
                curr_len = 1
        if curr_len > max_l:
            max_l = curr_len

        def solve_two(char1, char2, forbidden):
            res = 0

            for segment in s.split(forbidden):
                if not segment:
                    continue
                lookup = {0: -1}
                diff = 0
                for i, char in enumerate(segment):
                    if char == char1:
                        diff += 1
                    else:
                        diff -= 1

                    if diff in lookup:
                        length = i - lookup[diff]
                        if length > res:
                            res = length
                    else:
                        lookup[diff] = i
            return res

        max_l = max(max_l, solve_two("a", "b", "c"))
        max_l = max(max_l, solve_two("a", "c", "b"))
        max_l = max(max_l, solve_two("b", "c", "a"))

        lookup = {0: -1}
        d1, d2 = 0, 0
        OFFSET = 100001

        for i, char in enumerate(s):
            if char == "a":
                d1 += 1
            elif char == "b":
                d1 -= 1
                d2 += 1
            else:
                d2 -= 1

            key = d1 * OFFSET + d2
            if key in lookup:
                length = i - lookup[key]
                if length > max_l:
                    max_l = length
            else:
                lookup[key] = i

        return max_l
