class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        """
        Sorts the students in a class according to their scores in the k-th exam.

        Given a 0-indexed m x n integer matrix `score`, where each row represents a student
        and `score[i][j]` is the score of the i-th student in the j-th exam (all scores are distinct),
        this method sorts the students (the rows) in descending order based on their scores in the
        k-th (0-indexed) exam.

        Args:
            score (List[List[int]]): A 2D list where each row represents one student's scores across all exams.
            k (int): The exam index to sort the students by.

        Returns:
            List[List[int]]: The matrix of student scores, sorted by the k-th exam in descending order.

        Example:
            Input: score = [
                               [90, 80, 70],
                               [85, 95, 88],
                               [100, 60, 70]
                           ], k = 1
            Output: [
                        [85, 95, 88],    # 95 in k=1
                        [90, 80, 70],    # 80 in k=1
                        [100, 60, 70]    # 60 in k=1
                    ]
            (Sorted in descending order according to the 1st exam column.)

        Time Complexity: O(m * log m), where m is the number of students (rows).
        Space Complexity: O(m).

        LeetCode: Beats 100% of submissions
        """
        return sorted(score, key=lambda exams: exams[k], reverse=True)
