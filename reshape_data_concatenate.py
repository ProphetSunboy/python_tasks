import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Concatenates two DataFrames with identical columns (student_id, name, age)
    vertically into a single DataFrame.

    Args:
        df1 (pd.DataFrame): A DataFrame with the following columns:
            - student_id (int): The student's unique identifier.
            - name (object): The student's name.
            - age (int): The student's age.
        df2 (pd.DataFrame): Another DataFrame with the same columns as df1.

    Returns:
        pd.DataFrame: A new DataFrame containing all rows from df1 followed by
        all rows from df2.

    Example:
        Input:
            df1 =
               student_id   name  age
            0           1   Alice   20
            1           2     Bob   21

            df2 =
               student_id   name  age
            0           3  Charlie  22
            1           4   David   20

        Output:
           student_id   name  age
        0           1   Alice   20
        1           2     Bob   21
        0           3  Charlie  22
        1           4   David   20

    Time Complexity: O(n), where n is the total number of rows in both DataFrames.
    Space Complexity: O(n), for storing the concatenated DataFrame.

    LeetCode: Beats 92.86% of submissions
    """
    return pd.concat([df1, df2])
