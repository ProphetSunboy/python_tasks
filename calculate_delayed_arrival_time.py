class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        """
        Calculates the actual arrival time of a train given its scheduled arrival time
        and delay, both in hours (24-hour format).

        Args:
            arrivalTime (int): Scheduled arrival time in hours (0-23).
            delayedTime (int): Delay in hours (0-23).

        Returns:
            int: The actual arrival time in 24-hour format (0-23).

        Example:
            >>> findDelayedArrivalTime(22, 3)
            1

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return (arrivalTime + delayedTime) % 24
