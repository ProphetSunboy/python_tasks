class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Given a 0-indexed list of positive integers `nums`, you can perform an
        operation any number of times:
        select an index `i` (0 <= i < n - 1), and replace either `nums[i]` or
        `nums[i+1]` with gcd(nums[i], nums[i+1]).

        Returns the minimum number of operations required to make all elements of
        `nums` equal to 1.
        If it is impossible, return -1.

        Args:
            nums (List[int]): The input list of positive integers.

        Returns:
            int: The minimum number of operations to make every element 1, or -1 if not possible.

        Example:
            Input: nums = [2,6,3,4]
            Output: 4


        Time Complexity: O(n^2), where n is the length of nums (due to checking all sublists).
        Space Complexity: O(1) (ignoring input storage).

        LeetCode: Beats 100% of submissions
        """
        n = len(nums)

        overall_gcd = nums[0]
        for x in nums[1:]:
            overall_gcd = gcd(overall_gcd, x)
        if overall_gcd > 1:
            return -1

        ones = nums.count(1)
        if ones > 0:
            return n - ones

        min_len = float("inf")
        for i in range(n):
            curr_gcd = nums[i]
            for j in range(i + 1, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        if min_len == float("inf"):
            return -1

        return (min_len - 1) + (n - 1)
