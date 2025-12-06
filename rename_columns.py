import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Renames columns of the given DataFrame `students` according to the mapping:
        - 'id'    -> 'student_id'
        - 'first' -> 'first_name'
        - 'last'  -> 'last_name'
        - 'age'   -> 'age_in_years'

    Args:
        students (pd.DataFrame): DataFrame containing the original student data with columns
                                 ['id', 'first', 'last', 'age'].

    Returns:
        pd.DataFrame: DataFrame with renamed columns:
                      ['student_id', 'first_name', 'last_name', 'age_in_years']

    Example:
        Input:
            id  first   last    age
            1   John    Doe     20
            2   Jane    Smith   22

        Output:
            student_id  first_name  last_name  age_in_years
            1           John        Doe        20
            2           Jane        Smith      22

    Time Complexity: O(1), as renaming columns is a constant time operation.
    Space Complexity: O(N), where N is the number of rows in the DataFrame (for the copy with renamed columns).

    LeetCode: Beats 90.89% of submissions
    """
    return students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
