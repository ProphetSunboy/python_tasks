class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        """
        Finds the employee who worked on the task with the longest duration.

        There are n employees, each with a unique id from 0 to n - 1.

        Args:
            n (int): The number of employees.
            logs (List[List[int]]): A list of logs where each log is [employee_id, leave_time].
                - employee_id (int): The id of the employee who worked on the ith task.
                - leave_time (int): The time at which the employee finished the ith task.
                The ith task starts immediately after the (i-1)th task ends, and the 0th task starts at time 0.
                All leave_time values are unique.

        Returns:
            int: The id of the employee who worked the task with the longest duration.
                 If there is a tie, returns the smallest id among them.

        Example:
            >>> hardestWorker(3, [[0,3],[2,5],[0,9],[1,15]])
            1

        Time Complexity: O(m), where m is the number of logs.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        longest_task = logs[0][1]
        longest_id = logs[0][0]

        for i in range(1, len(logs)):
            curr_task = logs[i][1] - logs[i - 1][1]

            if curr_task > longest_task:
                longest_task = curr_task
                longest_id = logs[i][0]
            elif curr_task == longest_task and logs[i][0] < longest_id:
                longest_id = logs[i][0]

        return longest_id
