class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """Calculates the absolute difference between left and right sums for each element in a list.

        For each index i in the input list, computes the difference between:
        - Sum of all elements to the left of i (leftSum)
        - Sum of all elements to the right of i (rightSum)
        Returns a list of absolute differences.

        Args:
            nums (list[int]): Input list of integers

        Returns:
            list[int]: List where each element is |leftSum[i] - rightSum[i]|

        Examples:
            >>> leftRightDifference([10, 4, 8, 3])
            [15, 1, 11, 22]  # [|0-15|, |10-11|, |14-3|, |22-0|]
            >>> leftRightDifference([1])
            [0]  # No elements on either side

        Time complexity: O(n) - where n is length of nums list
        Space complexity: O(n) - for storing answer list

        LeetCode: Beats 100% of submissions
        """
        answer = [0] * len(nums)
        left_sum = 0
        right_sum = sum(nums) - nums[0]

        for i in range(len(nums) - 1):
            answer[i] = abs(left_sum - right_sum)
            left_sum += nums[i]
            right_sum -= nums[i + 1]

        answer[-1] = abs(left_sum - right_sum)

        return answer
