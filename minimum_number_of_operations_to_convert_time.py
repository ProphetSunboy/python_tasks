class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        """
        Given two strings, current and correct, representing two 24-hour times in the format "HH:MM",
        return the minimum number of operations required to convert current to correct.

        In one operation, you can increase the time by 1, 5, 15, or 60 minutes. You may perform any number of operations.

        Args:
            current (str): The current time in "HH:MM" format.
            correct (str): The target time in "HH:MM" format.

        Returns:
            int: The minimum number of operations needed to convert current to correct.

        Example:
            >>> convertTime("02:30", "04:35")
            3

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        min_ops = 0

        curr_mins = int(current[3:])
        curr_hours = int(current[0:2])
        correct_mins = int(correct[3:])
        correct_hours = int(correct[0:2])

        if correct_mins < curr_mins:
            correct_mins += 60
            curr_hours += 1

        diff = (correct_mins - curr_mins) // 15
        curr_mins += diff * 15
        min_ops += diff

        diff = (correct_mins - curr_mins) // 5
        curr_mins += diff * 5
        min_ops += diff

        diff = correct_mins - curr_mins
        curr_mins += diff
        min_ops += diff

        if correct_hours >= curr_hours:
            min_ops += correct_hours - curr_hours
        else:
            min_ops += correct_hours + (24 - curr_hours)

        return min_ops
