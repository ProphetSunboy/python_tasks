class Solution:
    def maximumTime(self, time: str) -> str:
        """
        Given a string `time` in the format "hh:mm", where some digits are hidden as '?',
        return the latest valid 24-hour time (between "00:00" and "23:59") that can be obtained
        by replacing each '?' with a digit.

        Args:
            time (str): The time string with possible hidden digits represented by '?'.

        Returns:
            str: The latest valid time string after replacing all '?'.

        Example:
            >>> maximumTime("2?:?0")
            '23:50'
            >>> maximumTime("0?:3?")
            '09:39'
            >>> maximumTime("1?:22")
            '19:22'

        Time Complexity: O(1) - The input is always a fixed-length string.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        res = ""

        for i, ch in enumerate(time):
            if ch == "?":
                if i == 0:
                    if time[1] != "?" and time[1] > "3":
                        res += "1"
                    else:
                        res += "2"
                elif i == 1:
                    if res[0] == "2":
                        res += "3"
                    else:
                        res += "9"
                elif i == 3:
                    res += "5"
                elif i == 4:
                    res += "9"
            else:
                res += ch

        return res
