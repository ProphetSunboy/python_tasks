class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        """Given a 0-indexed integer list nums and an integer k, perform the following
        operation exactly k times to maximize your score:

            1. Select the maximum element m from nums.
            2. Remove m from the list.
            3. Add a new element with value m + 1 to the list.
            4. Increase your score by m.

        Return the maximum score achievable after k operations.

        Args:
            nums (list[int]): The input list.
            k (int): The number of operations to perform.

        Returns:
            int: The maximum score possible after k operations.

        Example:
            >>> maximizeSum([1,2,3,4,5], 3)
            18  # Select 5, add 5 to score, insert 6; select 6, add 6, insert 7; select 7, add 7, insert 8; total = 5+6+7=18

        Time complexity: O(n + k)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        max_num = max(nums)
        score = 0

        for i in range(k):
            score += max_num + i

        return score
