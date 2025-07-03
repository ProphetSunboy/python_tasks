class Solution:
    def reformatDate(self, date: str) -> str:
        """Converts a date string from the format "Day Month Year" (e.g., "20th Oct 2052") to "YYYY-MM-DD".
        The input date string has:
            - Day: "1st" to "31st"
            - Month: "Jan", "Feb", ..., "Dec"
            - Year: 1900 to 2100

        Args:
            date (str): The date string in "Day Month Year" format.

        Returns:
            str: The reformatted date string in "YYYY-MM-DD" format.

        Examples:
            >>> reformatDate("20th Oct 2052")
            '2052-10-20'
            >>> reformatDate("6th Jun 1933")
            '1933-06-06

        LeetCode: Beats 100% of submissions
        """
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }

        converted = date.split()
        converted[0] = converted[0].zfill(4)[:2]
        converted[1] = months[converted[1]]

        return "-".join(reversed(converted))
