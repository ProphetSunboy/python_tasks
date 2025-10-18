class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        """
        Given an integer list nums and an integer k, find the maximum possible number of distinct elements
        after performing the following operation on each element at most once:

            - Add any integer in the range [-k, k] to that element.

        Args:
            nums (List[int]): The list of integers to process.
            k (int): The maximum absolute value of the integer that can be added or subtracted from each element.

        Returns:
            int: The largest number of distinct elements that can be achieved.

        Example:
            >>> maxDistinctElements([1,2,2,3], 1)
            4

        Time Complexity: O(n log n), where n is the length of nums (for sorting).
        Space Complexity: O(1) (not counting sort).
        """
        nums.sort()

        cnt = 0
        prev = float("-infinity")

        for num in nums:
            curr = min(max(num - k, prev + 1), num + k)
            if curr > prev:
                cnt += 1
                prev = curr

        return cnt
