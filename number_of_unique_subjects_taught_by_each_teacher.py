import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame 'teacher' with the columns:
        - teacher_id (int): The unique ID for each teacher.
        - subject_id (int): The unique ID for each subject.
        - dept_id (int): The department ID.

    Each row represents that the teacher with teacher_id teaches the subject
    with subject_id in the department dept_id.
    (subject_id, dept_id) together form the primary key.

    This function calculates the number of unique subjects each teacher teaches
    at the university.

    Args:
        teacher (pd.DataFrame): DataFrame containing columns 'teacher_id',
        'subject_id', and 'dept_id'.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - teacher_id (int): The unique ID for each teacher.
            - cnt (int): The count of unique subjects taught by each teacher.

    Example:
        Input:
            teacher =
               teacher_id  subject_id  dept_id
            0           1           2        3
            1           1           2        4
            2           1           3        3
            3           2           2        3

        Output:
           teacher_id  cnt
        0           1    2
        1           2    1

        Time Complexity: O(n), where n is the number of rows in 'teacher'.
        Space Complexity: O(n).

        LeetCode: Beats 95.63% of submissions
    """
    return teacher.groupby("teacher_id")["subject_id"].nunique().reset_index(name="cnt")
