class Solution:
    def splitNum(self, num: int) -> int:
        """Given a positive integer num, split its digits into two non-negative integers num1 and num2 such that:
            - The concatenation of num1 and num2 forms a permutation of the digits of num.
            - num1 and num2 can have leading zeros.
            - Return the minimum possible sum of num1 and num2.

        Args:
            num (int): The input positive integer.

        Returns:
            int: The minimum possible sum of num1 and num2 formed from the digits of num.

        Example:
            >>> splitNum(4325)
            59

        Time complexity: O(n), where n is the number of digits in num.
        Space complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        num1 = []
        num2 = []

        nums = sorted(str(num), reverse=True)

        if len(nums) % 2:
            nums.append("0")

        while nums:
            num1.append(nums.pop())
            num2.append(nums.pop())

        return int("".join(num1)) + int("".join(num2))
