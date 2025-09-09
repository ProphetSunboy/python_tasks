class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        Calculates the total number of seconds Ashe is poisoned after Teemo's attacks.

        When Teemo attacks at time t, Ashe is poisoned for exactly `duration` seconds,
        i.e., during [t, t + duration - 1]. If a new attack occurs before the previous
        poison effect ends, the timer resets and the poison effect extends accordingly.

        Args:
            timeSeries (List[int]): Non-decreasing list of times when Teemo attacks.
            duration (int): Duration (in seconds) of poison effect per attack.

        Returns:
            int: Total number of seconds Ashe is poisoned.

        Example:
            >>> findPoisonedDuration([1, 4], 2)
            4
            >>> findPoisonedDuration([1, 2], 2)
            3

        Time Complexity: O(n), where n is the length of timeSeries.
        Space Complexity: O(1).

        LeetCode: Beats 98.88% of submissions
        """
        total = 0
        last = -1

        for i in timeSeries:
            if i > last:
                total += duration
            else:
                total += duration - (last + 1 - i)

            last = i + duration - 1

        return total
