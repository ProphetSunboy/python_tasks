class Solution:
    def minBitwiseArray(self, nums):
        """
        Given a list `nums` consisting of n prime integers, construct a list `ans` of length n such that,
        for each index i, the bitwise OR of `ans[i]` and `ans[i] + 1` equals `nums[i]`, i.e.,
        (ans[i] | (ans[i] + 1)) == nums[i].

        Each value of `ans[i]` should be minimized. If it is not possible to find
        such a value for `ans[i]`, set ans[i] = -1.

        Args:
            nums (List[int]): List of n prime integers.

        Returns:
            List[int]: List of length n, each value constructed as described,
                or -1 if not possible.

        Example:
            Input: nums = [2,3,5,7]
            Output: [-1,1,4,3]

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        ans = []

        for p in nums:
            if p == 2:
                ans.append(-1)
                continue

            k = 0
            while (p >> k) & 1:
                k += 1

            x = p - (1 << (k - 1))

            if (x | (x + 1)) == p:
                ans.append(x)
            else:
                ans.append(-1)

        return ans
