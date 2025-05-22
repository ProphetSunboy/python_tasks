from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
        Write a program to count the number of days between two dates.

        The two dates are given as strings, their format is YYYY-MM-DD.

        :param str date1: string in format YYYY-MM-DD
        :param str date2: string in format YYYY-MM-DD
        :returns int: number of days between date1 and date2

        Time complexity: O(1)
        Space complexity: O(1)

        LeetCode: Beats 100%
        """
        return abs(
            (
                datetime(*list(map(int, date1.split("-"))))
                - datetime(*list(map(int, date2.split("-"))))
            ).days
        )
