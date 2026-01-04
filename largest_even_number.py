class Solution:
    def largestEven(self, s: str) -> str:
        """
        Given a string s consisting only of the characters '1' and '2',
        you may delete any number of characters from s without changing
        the order of the remaining characters.

        Return the largest possible resultant string that represents an
        even integer. If there is no such string, return the empty
        string "".

        Args:
            s (str): Input string consisting of only '1' and '2'.

        Returns:
            str: Largest possible even integer represented as a string,
                or an empty string if not possible.

        Example:
            Input: s = "11211"
            Output: "112"
            Input: s = "111"
            Output: ""

        Time Complexity: O(n), where n is the length of the input string.
        Space Complexity: O(n), to store the resulting string.

        LeetCode: Beats 100% of submissions
        """
        nums = list(s)

        while len(nums) > 0 and nums[-1] != "2":
            nums.pop()

        return "".join(nums)
