class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        """
        Given a 0-indexed integer list nums of even length, repeatedly:

            1. Remove the minimum number from nums.
            2. Remove the maximum number from nums.
            3. Calculate the average of the two removed numbers: (min + max) / 2.

        Continue until nums is empty. Return the number of distinct averages obtained during this process.

        Args:
            nums (list[int]): An even-length list of integers.

        Returns:
            int: The number of distinct averages calculated.

        Example:
            >>> distinctAverages([4,1,4,0,3,5])
            2

        Time Complexity: O(n log n), due to sorting.
        Space Complexity: O(n), for the set and deque.

        LeetCode: Beats 100% of submissions
        """
        averages = set()
        d = deque(sorted(nums))

        while d:
            averages.add((d.popleft() + d.pop()) / 2)

        return len(averages)
