class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        Given a 0-indexed integer list nums, where nums[i] represents the score
        of the ith student, and an integer k, select the scores of any k students
        such that the difference between the highest and lowest of the selected
        k scores is minimized.

        Returns the minimum possible difference.

        Args:
            nums (List[int]): List of student scores.
            k (int): Number of students to select.

        Returns:
            int: The minimum possible difference between the highest and lowest scores among any group of k students.

        Example:
            >>> minimumDifference([90, 85, 75, 60, 120], 3)
            15

        Time Complexity: O(n log n), where n is the length of nums (due to sorting).
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        nums.sort()

        min_diff = float("inf")
        i = 0
        j = k - 1
        while j < len(nums):
            if nums[j] - nums[i] < min_diff:
                min_diff = nums[j] - nums[i]

            i += 1
            j += 1

        return min_diff
