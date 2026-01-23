class Solution:
    def validStrings(self, n: int) -> List[str]:
        """
        Given a positive integer n, return all binary strings of length n such that
        every substring of length 2 contains at least one '1'.

        A binary string x is valid if all substrings of x of length 2 contain
        at least one "1". Return all valid strings with length n, in any order.

        Args:
            n (int): The length of the binary strings.

        Returns:
            List[str]: A list of all valid binary strings of length n.

        Example:
            Input: n = 3
            Output: ["010","011","101","110","111"]

        Time Complexity: O(n * 2^n), where n is the length of the string.
        Space Complexity: O(2^n)
        """
        strs = set(["0", "1"])
        curr_len = 1

        while curr_len < n:
            curr = set()

            while strs:
                s = strs.pop()

                if s[-1] == "0":
                    curr.add(s + "1")
                else:
                    curr.add(s + "0")
                    curr.add(s + "1")

            strs = curr
            curr_len += 1

        return strs
