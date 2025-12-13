import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    """
    Creates a pandas DataFrame from a 2D list of student data.

    Each inner list in student_data should represent a student, containing:
        - student_id (int)
        - age (int)

    The resulting DataFrame will have two columns: "student_id" and "age",
    and preserve the order of student_data.

    Args:
        student_data (List[List[int]]): 2D list where each sublist is [student_id, age].

    Returns:
        pd.DataFrame: DataFrame with columns ["student_id", "age"].

    Example:
        >>> createDataframe([[1, 15], [2, 18], [3, 16]])
           student_id  age
        0           1   15
        1           2   18
        2           3   16

    Time Complexity: O(N), where N is the number of students.
    Space Complexity: O(N).

    LeetCode: Beats 91.49% of submissions
    """
    return pd.DataFrame(student_data, columns=["student_id", "age"])
