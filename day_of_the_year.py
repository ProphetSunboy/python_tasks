class Solution:
    def dayOfYear(self, date: str) -> int:
        """
        Given a string date representing a Gregorian calendar date formatted as
        YYYY-MM-DD, return the day number of the year.

        Leetcode Beats 97.27%
        """
        leap_y = {
            1: 31,
            2: 60,
            3: 91,
            4: 121,
            5: 152,
            6: 182,
            7: 213,
            8: 244,
            9: 274,
            10: 305,
            11: 335,
            12: 366,
        }
        com_y = {
            1: 31,
            2: 59,
            3: 90,
            4: 120,
            5: 151,
            6: 181,
            7: 212,
            8: 243,
            9: 273,
            10: 304,
            11: 334,
            12: 365,
        }
        d = date.split("-")

        y = int(d[0])
        if y % 100 and y % 4 == 0 or y % 400 == 0:
            return leap_y.get(int(d[1]) - 1, 0) + int(d[2])

        return com_y.get(int(d[1]) - 1, 0) + int(d[2])
