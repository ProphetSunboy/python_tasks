class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        Given a list nums, you can repeatedly perform the following operation:

            1. Select the adjacent pair of numbers with the minimum sum (if multiple, choose the leftmost).
            2. Replace this pair by their sum (removing one element).

        Return the minimum number of such operations needed to make the list non-decreasing (i.e., nums[i] >= nums[i-1] for all i > 0).

        Args:
            nums (List[int]): The initial list of integers.

        Returns:
            int: The minimum number of operations required to make nums non-decreasing.

        Example:
            >>> minimumPairRemoval([5, 2, 3, 1])
            2

        Time Complexity: O(n^2), where n is the length of nums (since each operation may scan the list).
        Space Complexity: O(1) (modifies nums in-place).

        LeetCode: Beats 98.76% of submissions
        """
        ops = 0

        while True:
            flag = False
            min_pair = 10**4
            min_idx = -1
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    flag = True
                if nums[i] + nums[i + 1] < min_pair:
                    min_pair = nums[i] + nums[i + 1]
                    min_idx = i

            if not flag:
                break

            n = nums.pop(min_idx)
            nums[min_idx] += n
            ops += 1

        return ops
