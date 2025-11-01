class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        Returns all possible times the binary watch could represent with a given number of LEDs turned on.

        A binary watch has:
            - 4 LEDs for the hour (0-11)
            - 6 LEDs for the minute (0-59)
        Each LED represents a binary digit (bit), with lowest significant bit on the right.

        Args:
            turnedOn (int): Number of LEDs that are currently on.

        Returns:
            List[str]: A list of times formatted as "H:MM", where hour has no leading zeros
                       and minute always has two digits with leading zero if needed.

        Example:
            >>> readBinaryWatch(1)
            ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']

        Time Complexity: O(720), since there are 12 hours and 60 minutes (constant).
        Space Complexity: O(1), not counting the output list.

        LeetCode: Beats 100% of submissions
        """
        result = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        return result
