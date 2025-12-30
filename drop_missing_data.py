import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Removes rows from the students DataFrame where the 'name' column contains
    missing values (NaN).

    Args:
        students (pd.DataFrame): A DataFrame with columns:
            - student_id (int)
            - name (object)
            - age (int)

    Returns:
        pd.DataFrame: A new DataFrame with rows containing missing values in
        the 'name' column removed.

    Example:
        Input:
            student_id   name    age
            1            Alice   20
            2            NaN     19
            3            Bob     21

        Output:
            student_id   name    age
            1            Alice   20
            3            Bob     21

    Time Complexity: O(n), where n is the number of rows in the DataFrame.
    Space Complexity: O(n), for storing the result DataFrame.

    LeetCode: Beats 98.18% of submissions
    """
    return students.dropna(subset="name")
