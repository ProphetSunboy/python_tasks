class Solution:
    def findLatestTime(self, s: str) -> str:
        """Finds the latest possible 12-hour time by replacing '?' characters.

        Given a string `s` representing a 12-hour format time ("HH:MM") where
        some digits are replaced with '?', this function replaces each '?' with a
        digit to form the latest possible valid time.

        A valid 12-hour time is in the format "HH:MM", where HH is between 00
        and 11, and MM is between 00 and 59.

        Args:
            s (str): The input time string, possibly containing '?'.

        Returns:
            str: The string representing the latest possible valid time.

        Example:
            Input: s = "1?:?4"
            Output: "11:54"
            Explanation: The latest hour starting with '1' is 11. The latest
                         minute ending with '4' is 54.

        Time complexity: O(1), as the input string has a fixed length of 5.
        Space complexity: O(1), for the output string.

        LeetCode: Beats 95.78% of submissions
        """
        pos = {0: "1", 1: "1", 3: "5", 4: "9"}
        latest = ""

        for i, ch in enumerate(s):
            if ch.isdigit():
                latest += ch
            else:
                if i == 0 and s[1] > "1" and s[1].isdigit():
                    latest += "0"
                elif i == 1 and latest[-1] == "0":
                    latest += "9"
                else:
                    latest += pos.get(i, ":")

        return latest
