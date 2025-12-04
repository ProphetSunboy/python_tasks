import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """
    Converts the 'grade' column in the students DataFrame from float to integer type.

    Args:
        students (pd.DataFrame): A DataFrame containing the following columns:
            - student_id (int)
            - name (object)
            - age (int)
            - grade (float)

    Returns:
        pd.DataFrame: The input DataFrame with the 'grade' column converted to integers.

    Example:
        Input:
            student_id  name   age  grade
            1           John   18   87.8
            2           Jane   19   90.0

        Output:
            student_id  name   age  grade
            1           John   18   87
            2           Jane   19   90

    Time Complexity: O(N), where N is the number of rows in the DataFrame.
    Space Complexity: O(1), as the operation modifies data in-place
    without additional storage.

    LeetCode: Beats 96.89% of submissions
    """
    students["grade"] = students["grade"].astype(int)
    return students
