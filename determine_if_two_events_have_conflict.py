class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        """
        Determines if two events on the same day have a time conflict.

        Each event is represented as a list of two strings: [startTime, endTime],
        where times are in "HH:MM" 24-hour format and intervals are inclusive.

        A conflict exists if the two events overlap at any moment.

        Args:
            event1 (list[str]): [startTime1, endTime1] for the first event.
            event2 (list[str]): [startTime2, endTime2] for the second event.

        Returns:
            bool: True if the events conflict (overlap), False otherwise.

        Example:
            >>> haveConflict(["01:15", "02:00"], ["02:00", "03:00"])
            True

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return (event1[1] <= event2[1] and event1[1] >= event2[0]) or (
            event2[1] <= event1[1] and event2[1] >= event1[0]
        )
