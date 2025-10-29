class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        """
        Calculates the total number of days Alice and Bob are in Rome together.

        Alice and Bob each visit Rome over their respective date ranges within the same (non-leap) year.
        Arrival and departure dates are given as 5-character strings in the format "MM-DD".

        Args:
            arriveAlice (str): Alice's arrival date in "MM-DD" format.
            leaveAlice (str): Alice's departure date in "MM-DD" format.
            arriveBob (str): Bob's arrival date in "MM-DD" format.
            leaveBob (str): Bob's departure date in "MM-DD" format.

        Returns:
            int: Total number of overlapping days Alice and Bob are in Rome together.

        Example:
            >>> countDaysTogether("08-15", "08-18", "08-16", "08-19")
            3

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def date_to_day(date: str) -> int:
            month, day = map(int, date.split("-"))
            return sum(days_per_month[: month - 1]) + day

        a1, a2 = date_to_day(arriveAlice), date_to_day(leaveAlice)
        b1, b2 = date_to_day(arriveBob), date_to_day(leaveBob)

        start = max(a1, b1)
        end = min(a2, b2)

        return max(0, end - start + 1)
