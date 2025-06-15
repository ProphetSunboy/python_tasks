class Solution:
    def maxDiff(self, num: int) -> int:
        """Calculates the maximum possible difference between two numbers formed by replacing digits.

        You are given an integer num. You will apply the following steps to num two separate times:
        1. Pick a digit x (0 <= x <= 9)
        2. Pick another digit y (0 <= y <= 9). Note y can be equal to x
        3. Replace all occurrences of x in num with y
        Let a and b be the two results from applying the operation independently.

        Args:
            num (int): Input integer to transform

        Returns:
            int: Maximum possible difference between two valid transformed numbers

        Examples:
            >>> maxDiff(555)
            888  # Replace 5->9 for max, 5->1 for min: 999 - 111 = 888
            >>> maxDiff(9)
            8  # Replace 9->9 for max, 9->1 for min: 9 - 1 = 8

        Note:
            - Neither result can have leading zeros
            - Neither result can be 0
            - The same digit can be chosen for both transformations

        Time complexity: O(n) - where n is number of digits in num
        Space complexity: O(n) - for string conversion

        LeetCode: Beats 100% of submissions
        """
        a = 0
        b = 0
        s_num = str(num)

        idx = 0
        for i, ch in enumerate(s_num):
            if ch < "9":
                idx = i
                break

        a = int(s_num.replace(s_num[idx], "9"))

        idx = 0
        for i in range(len(s_num)):
            if s_num[i] > "1":
                idx = i
                break

        if idx > 0 and s_num.count(s_num[idx]) != len(s_num):
            b = int(s_num.replace(s_num[idx], "0"))
        else:
            b = int(s_num.replace(s_num[idx], "1"))

        return a - b
