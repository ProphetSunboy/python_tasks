import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame `students` with the following schema:

        +-------------+--------+
        | Column Name | Type   |
        +-------------+--------+
        | student_id  | int    |
        | name        | object |
        | age         | int    |
        +-------------+--------+

    This function selects the name and age of the student with student_id = 101.

    Args:
        students (pd.DataFrame): DataFrame containing student information.

    Returns:
        pd.DataFrame: DataFrame with columns 'name' and 'age' for the student
        whose student_id is 101.

    Example:
        Input DataFrame:
            student_id  name      age
            101         Alice     23
            102         Bob       21

        Output DataFrame:
            name      age
            Alice     23

    Time Complexity: O(M), where M is the number of students (since we scan the DataFrame to match student_id).
    Space Complexity: O(1), since a small subset of rows/columns is returned.

    LeetCode: Beats 97.66% of submissions
    """
    return students[students["student_id"] == 101][["name", "age"]]
