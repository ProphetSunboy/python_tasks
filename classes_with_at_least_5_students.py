import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the names of all classes that have at least five students enrolled.

    Args:
        courses (pd.DataFrame): DataFrame with columns:
            - 'student': student name (str)
            - 'class': class name (str)
        Each row represents a student enrolled in a class.

    Returns:
        pd.DataFrame: DataFrame containing a single column 'class' with class
        names having at least five students.

    Example:
        Input:
            courses = pd.DataFrame({
                'student': ['A', 'B', 'C', 'D', 'E', 'F', 'A'],
                'class':   ['Math', 'Math', 'Math', 'Math', 'Math', 'Math', 'History']
            })
        Output:
                class
            0    Math

    Time Complexity: O(n), where n is the number of rows in courses.
    Space Complexity: O(k), where k is the number of unique classes.

    LeetCode: Beats 94.48% of submissions
    """
    classes_freq = courses["class"].value_counts()
    return classes_freq[classes_freq >= 5].reset_index().drop("count", axis=1)
