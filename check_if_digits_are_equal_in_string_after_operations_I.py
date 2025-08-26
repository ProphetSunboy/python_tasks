class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        Given a string s consisting of digits, repeatedly perform the following operation until the string has exactly two digits:

            - For each pair of consecutive digits in s (from left to right), compute a new digit as (digit1 + digit2) % 10.
            - Replace s with the sequence of these newly computed digits, preserving their order.

        Return True if the final two digits are equal, otherwise return False.

        Args:
            s (str): The input string of digits.

        Returns:
            bool: True if the final two digits are equal, False otherwise.

        Example:
            >>> hasSameDigits("12345")
            False
            >>> hasSameDigits("1111")
            True

        Time Complexity: O(n^2), where n is the length of s.
        Space Complexity: O(n), for storing intermediate digit lists.

        LeetCode: Beats 97.16% of submissions
        """
        nums = list(map(int, s))

        while len(nums) > 2:
            curr = []

            for i in range(len(nums) - 1):
                curr.append((nums[i] + nums[i + 1]) % 10)

            nums = curr

        return nums[0] == nums[1]
