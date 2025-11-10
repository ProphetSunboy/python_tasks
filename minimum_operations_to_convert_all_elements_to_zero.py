class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Given a list nums of size n consisting of non-negative integers,
        return the minimum number of operations required to make all elements 0.

        In one operation, you may select any sublist [i, j] (0 <= i <= j < n)
        and set all occurrences of the smallest (minimum) non-zero value in that
        sublist to 0.

        Args:
            nums (List[int]): List of non-negative integers.

        Returns:
            int: The minimum number of operations to make all elements zero.

        Example:
            Input: nums = [1,2,1,2,1,2]
            Output: 4

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), due to use of an auxiliary stack.
        """
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
