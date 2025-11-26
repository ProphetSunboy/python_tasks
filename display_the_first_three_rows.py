import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Display the first 3 rows of the `employees` DataFrame.

    Args:
        employees (pd.DataFrame): A DataFrame containing employee data with the following columns:
            - employee_id (int)
            - name (object)
            - department (object)
            - salary (int)

    Returns:
        pd.DataFrame: A DataFrame consisting of the first 3 rows of the input DataFrame.

    Example:
        Given the following DataFrame:
           employee_id     name department  salary
        0            1    Alice         HR   70000
        1            2      Bob         IT   80000
        2            3  Charlie         HR   75000
        3            4    David      Sales   72000

        The function will return the first 3 rows:
           employee_id     name department  salary
        0            1    Alice         HR   70000
        1            2      Bob         IT   80000
        2            3  Charlie         HR   75000

    Time Complexity: O(1) (since selecting the first 3 rows is a constant-time operation).
    Space Complexity: O(1) (returns a view/slice, memory proportional to 3 rows).

    LeetCode: Beats 90.54% of submissions
    """
    return employees.iloc[:3]
