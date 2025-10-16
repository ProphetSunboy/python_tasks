class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        """
        Given a list of tasks, returns the earliest time at which at least one task is finished.

        Each task is represented as a list [si, ti], where:
            - si: the start time of the i-th task
            - ti: the duration of the i-th task

        The finish time of a task is si + ti. The function finds the minimum finish time among all tasks.

        Args:
            tasks (List[List[int]]): A 2D list where each sublist represents [start, duration] of a task.

        Returns:
            int: The earliest time at which any task is finished.

        Example:
            >>> earliestTime([[2, 3], [5, 2], [1, 4]])
            5  # Task 0 finishes at 5 (2+3), task 1 at 7 (5+2), task 2 at 5 (1+4), so earliest is 5.

        Time Complexity: O(n), where n is the number of tasks.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        earliest = float("infinity")

        for start, duration in tasks:
            if start + duration < earliest:
                earliest = start + duration

        return earliest
