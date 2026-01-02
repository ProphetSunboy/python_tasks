# First solution
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        """
        You are given an integer array nums with the following properties:

            nums.length == 2 * n.
            nums contains n + 1 unique elements.
            Exactly one element of nums is repeated n times.

        Return the element that is repeated n times.
        """
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
                if counter[num] > 1:
                    return num


# Second solution
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
        Given an integer list nums of length 2 * n, where there are n + 1
        unique elements and exactly one element appears n times, return the
        element that is repeated n times.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The element that is repeated n times.

        Example:
            Input: nums = [1,2,3,3]
            Output: 3

            Input: nums = [2,1,2,5,3,2]
            Output: 2

        Time Complexity: O(n), where n is half the length of nums.
        Space Complexity: O(n), for storing seen elements.

        LeetCode: Beats 100% of submissions
        """
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num)

        return 0
