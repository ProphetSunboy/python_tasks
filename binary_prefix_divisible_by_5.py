# First solution
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """
        You are given a binary list nums (0-indexed).

        We define xi as the number whose binary representation is the subarray
        nums[0..i] (from most-significant-bit to least-significant-bit).

            For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.

        Return a list of booleans answer where answer[i] is True if xi is
        divisible by 5.

        :param list[int] nums: binary list
        :returns list[bool] answer: answer[i] is True if xi is divisible by 5

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 97.87%
        """
        res = []
        num = 0

        for n in nums:
            num = (num * 2 + n) % 5
            res.append(num == 0)

        return res


# Second solution
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """
        Given a binary list nums (0-indexed), computes for each prefix
        nums[0..i] whether its value is divisible by 5.

        xi is defined as the number whose binary representation is nums[0]
        (most-significant-bit) to nums[i] (least-significant-bit).
        For example, if nums = [1, 0, 1], then x0 = 1, x1 = 2, and x2 = 5.

        Returns a list of booleans answer such that answer[i] is True if xi is
        divisible by 5, otherwise False.

        Args:
            nums (List[int]): A list of 0s and 1s representing the binary digits.

        Returns:
            List[bool]: A list where answer[i] is True if prefix xi
            (from nums[0..i]) is divisible by 5.

        Example:
            Input: nums = [0,1,1]
            Prefixes and values: x0=0, x1=1, x2=3
            Output: [True, False, False]

            Input: nums = [1,0,1]
            Prefixes and values: x0=1, x1=2, x2=5
            Output: [False, False, True]

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        res = []
        num = 0

        for n in nums:
            num = ((num << 1) + n) % 5
            res.append(num == 0)

        return res
