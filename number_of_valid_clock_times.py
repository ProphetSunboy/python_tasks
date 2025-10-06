class Solution:
    def countTime(self, time: str) -> int:
        """
        Given a string `time` of length 5 representing the current time on a digital
        clock in the format "hh:mm", where some digits may be unknown and represented
        by '?', return the number of valid clock times that can be created by
        replacing every '?' with a digit from 0 to 9.

        The earliest possible time is "00:00" and the latest is "23:59".

        Args:
            time (str): The time string in the format "hh:mm", possibly containing '?'.

        Returns:
            int: The number of valid clock times that can be formed.

        Example:
            >>> countTime("2?:?0")
            24
            >>> countTime("0?:0?")
            100

        Time Complexity: O(1) — constant time, as the string is always of length 5.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        answer = 1

        if time[0] == "?":
            if time[1] < "4" or time[1] == "?":
                answer *= 3
            else:
                answer *= 2
        if time[1] == "?":
            if time[0] == "2":
                answer *= 4
            elif time[0] == "0" or time[0] == "1":
                answer *= 10
            else:
                answer *= 8
        if time[3] == "?":
            answer *= 6
        if time[4] == "?":
            answer *= 10

        return answer
