class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        """
        Given an even length list nums of n integers, repeatedly remove the smallest and largest elements,
        compute their average, and collect these averages. Return the minimum average obtained.

        The process:
            - While nums is not empty:
                - Remove the smallest element (minElement) and the largest element (maxElement)
                - Compute their average: (minElement + maxElement) / 2
                - Add this average to a list of averages
            - After all pairs are processed, return the minimum value in the averages list.

        Args:
            nums (list[int]): List of even length containing integers.

        Returns:
            float: The minimum average of all (minElement + maxElement) / 2 pairs.

        Example:
            >>> minimumAverage([1, 3, 5, 7])
            4.0

        Time Complexity: O(n log n), due to sorting.
        Space Complexity: O(1), not counting input and output.

        LeetCode: Beats 100% of submissions
        """
        min_avg = 51
        i, j = 0, len(nums) - 1
        nums.sort()

        while i < j:
            if (nums[i] + nums[j]) / 2 < min_avg:
                min_avg = (nums[i] + nums[j]) / 2

            i += 1
            j -= 1

        return min_avg
