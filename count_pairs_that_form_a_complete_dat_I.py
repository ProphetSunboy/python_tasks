class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        """
        Given an integer list `hours` representing times in hours, return the number of pairs (i, j)
        with i < j such that hours[i] + hours[j] is a multiple of 24 (i.e., forms a complete day).

        A complete day is any time duration that is an exact multiple of 24 hours (e.g., 24, 48, 72, ...).

        Args:
            hours (List[int]): List of time durations in hours.

        Returns:
            int: The number of valid pairs whose sum is a multiple of 24.

        Example:
            >>> countCompleteDayPairs([24, 48, 1, 23, 25])
            3

        Time Complexity: O(n), where n is the length of hours.
        Space Complexity: O(1) (since the remainder count is bounded by 24).

        LeetCode: Beats 100% of submissionss
        """
        complete_pairs = 0
        complete_days = 0
        remainder_count = defaultdict(int)

        for hour in hours:
            remainder = hour % 24

            if remainder == 0:
                complete_pairs += complete_days
                complete_days += 1
            else:
                complement = (24 - remainder) % 24
                complete_pairs += remainder_count[complement]

            remainder_count[remainder] += 1

        return complete_pairs
