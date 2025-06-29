class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        """Count the number of students doing homework at a given query time.

        Given two integer lists startTime and endTime and an integer queryTime,
        where the ith student started doing their homework at startTime[i] and
        finished at endTime[i], return the number of students who were doing
        homework at the specific queryTime. A student is considered to be doing
        homework if queryTime falls within their homework interval [startTime[i], endTime[i]]
        inclusive.

        Args:
            startTime (list[int]): List where startTime[i] is the start time of the ith student.
            endTime (list[int]): List where endTime[i] is the end time of the ith student.
            queryTime (int): The specific time to check how many students are doing homework.

        Returns:
            int: The number of students doing homework at queryTime.

        Example:
            >>> busyStudent([1, 2, 3], [3, 2, 7], 4)
            1
            >>> busyStudent([4], [4], 4)
            1
            >>> busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7)
            0

        LeetCode: Beats 100% of submissions
        """
        students = 0

        for i, time in enumerate(startTime):
            if queryTime >= time:
                if queryTime <= endTime[i]:
                    students += 1

        return students
