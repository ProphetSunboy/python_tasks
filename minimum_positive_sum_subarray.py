class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        """
        Find the minimum sum of a positive sublist within a given length range.

        Given an integer list nums and two integers l and r, this function finds
        the minimum sum of any sublist whose length is between l and r (inclusive),
        and whose sum is strictly greater than 0. If such a sublist does not exist,
        return -1.

        - A sublist is a contiguous non-empty sequence of elements in the list.

        Args:
            nums (List[int]): The input integer list.
            l (int): The minimum length of the sublist.
            r (int): The maximum length of the sublist.

        Returns:
            int: The minimum positive sublist sum in the range [l, r], or -1 if none exists.

        Example:
            >>> minimumSumSubarray([1, -2, 3, 4, -1], 2, 3)
            1

        Time Complexity: O(N * (r - l + 1)), where N is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 92.38% of submissions
        """
        min_sum = float("infinity")

        for i in range(len(nums)):
            curr = sum(nums[i : i + l - 1])

            for j in range(i + l - 1, min(len(nums), i + r)):
                curr += nums[j]

                if curr > 0 and curr < min_sum:
                    min_sum = curr

        return min_sum if min_sum < float("infinity") else -1
