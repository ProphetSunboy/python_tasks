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