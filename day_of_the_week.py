class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """
        Given a date, return the corresponding day of the week for that date.

        The input is given as three integers representing the day, month and
        year respectively.

        Return the answer as one of the following values {"Sunday", "Monday",
        "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.


        LeetCode Beats 100%
        """
        days = {
            0: "Saturday",
            1: "Sunday",
            2: "Monday",
            3: "Tuesday",
            4: "Wednesday",
            5: "Thursday",
            6: "Friday",
        }
        month_code = {
            1: 1,
            2: 4,
            3: 4,
            4: 0,
            5: 2,
            6: 5,
            7: 0,
            8: 3,
            9: 6,
            10: 1,
            11: 4,
            12: 6,
        }
        month_code_leap = {
            1: 0,
            2: 3,
            3: 4,
            4: 0,
            5: 2,
            6: 5,
            7: 0,
            8: 3,
            9: 6,
            10: 1,
            11: 4,
            12: 6,
        }
        century_code = {19: 0, 20: 6, 21: 4}

        year_code = (century_code[year // 100] + year % 100 + year % 100 // 4) % 7

        week_day = 0
        if year % 100 and year % 4 == 0 or year % 400 == 0:
            week_day = (day + month_code_leap[month] + year_code) % 7
        else:
            week_day = (day + month_code[month] + year_code) % 7

        return days[week_day]
