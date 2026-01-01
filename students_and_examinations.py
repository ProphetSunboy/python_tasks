import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    """
    Given three dataframes representing students, subjects, and examinations,
    return a dataframe showing the number of times each student attended each exam.

    Tables:
        Students:
            - student_id (int): Primary key, unique identifier for each student.
            - student_name (str): Name of the student.
        Subjects:
            - subject_name (str): Primary key, unique subject name.
        Examinations:
            - student_id (int): ID of the student who attended the exam.
            - subject_name (str): Name of the subject of the exam.
            (May contain duplicates for multiple attendances.)

    For every combination of student and subject, count how many times the
    student attended that subject's exam.
    The output is a dataframe ordered by student_id and subject_name, with columns:
        - student_id
        - student_name
        - subject_name
        - attended_exams (int): Number of times the exam was attended.

    Args:
        students (pd.DataFrame): DataFrame of students.
        subjects (pd.DataFrame): DataFrame of subjects.
        examinations (pd.DataFrame): DataFrame of exam attendances.

    Returns:
        pd.DataFrame: DataFrame with the number of times each student attended each exam,
                      ordered by student_id and subject_name.

    Example:
            Students table:
            +------------+--------------+
            | student_id | student_name |
            +------------+--------------+
            | 1          | Alice        |
            | 2          | Bob          |
            | 13         | John         |
            | 6          | Alex         |
            +------------+--------------+
            Subjects table:
            +--------------+
            | subject_name |
            +--------------+
            | Math         |
            | Physics      |
            | Programming  |
            +--------------+
            Examinations table:
            +------------+--------------+
            | student_id | subject_name |
            +------------+--------------+
            | 1          | Math         |
            | 1          | Physics      |
            | 1          | Programming  |
            | 2          | Programming  |
            | 1          | Physics      |
            | 1          | Math         |
            | 13         | Math         |
            | 13         | Programming  |
            | 13         | Physics      |
            | 2          | Math         |
            | 1          | Math         |
            +------------+--------------+
            Output:
            +------------+--------------+--------------+----------------+
            | student_id | student_name | subject_name | attended_exams |
            +------------+--------------+--------------+----------------+
            | 1          | Alice        | Math         | 3              |
            | 1          | Alice        | Physics      | 2              |
            | 1          | Alice        | Programming  | 1              |
            | 2          | Bob          | Math         | 1              |
            | 2          | Bob          | Physics      | 0              |
            | 2          | Bob          | Programming  | 1              |
            | 6          | Alex         | Math         | 0              |
            | 6          | Alex         | Physics      | 0              |
            | 6          | Alex         | Programming  | 0              |
            | 13         | John         | Math         | 1              |
            | 13         | John         | Physics      | 1              |
            | 13         | John         | Programming  | 1              |
            +------------+--------------+--------------+----------------+

    Time Complexity: O(s * t), where s is the number of students and t is the number of subjects.
    Space Complexity: O(s * t), for the output DataFrame with all student-subject pairs.

    LeetCode: Beats 96.54% of submissions
    """
    attended = (
        examinations.groupby(["student_id", "subject_name"])
        .size()
        .reset_index()
        .rename(columns={0: "attended"})
    )
    student_exams = students.merge(subjects, how="cross")

    student_exams["exams"] = 0
    merged_df = student_exams.merge(
        attended,
        how="left",
        left_on=["student_id", "subject_name"],
        right_on=["student_id", "subject_name"],
    )

    merged_df["attended_exams"] = np.maximum(
        merged_df["exams"], merged_df["attended"]
    ).fillna(0)

    return merged_df.drop(["exams", "attended"], axis=1).sort_values(
        by=["student_id", "subject_name"]
    )
