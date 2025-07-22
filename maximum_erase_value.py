class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        """Given a list of positive integers `nums`, find the maximum possible sum
        of a sublist containing only unique elements. You may erase exactly one
        such sublist, and the score is the sum of its elements.

        A sublist is a contiguous part of the list.

        Args:
            nums (list[int]): The input list of positive integers.

        Returns:
            int: The maximum sum of a sublist with all unique elements.

        Example:
            >>> maximumUniqueSubarray([4,2,4,5,6])
            17
            # The subarray [2,4,5,6] has all unique elements and sum 17.

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n), for tracking unique elements in the current window.
        """
        curr = []
        max_score = 0
        curr_score = 0

        for num in nums:
            if num not in curr:
                curr.append(num)
                curr_score += num
            else:
                if curr_score > max_score:
                    max_score = curr_score

                curr = curr[curr.index(num) + 1 :]
                curr.append(num)
                curr_score = sum(curr)

        if curr_score > max_score:
            max_score = curr_score

        return max_score
