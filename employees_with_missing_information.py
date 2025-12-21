import pandas as pd


def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame containing the IDs of all employees with missing
    information (either missing name or salary).

    Args:
        employees (pd.DataFrame): DataFrame with columns 'employee_id' and 'name'.
        salaries (pd.DataFrame): DataFrame with columns 'employee_id' and 'salary'.

    Returns:
        pd.DataFrame: DataFrame with a single column 'employee_id', containing
        employee IDs with missing name or salary, sorted in ascending order.

    Example:
        Input:
            employees = pd.DataFrame({"employee_id": [2, 4, 1], "name": ["Alice", "Bob", "Charlie"]})
            salaries = pd.DataFrame({"employee_id": [1, 2, 3], "salary": [1000, 1500, 1200]})
        Output:
            pd.DataFrame({"employee_id": [3, 4]})

    Time Complexity: O(N).
    Space Complexity: O(1).

    LeetCode: Beats 95.89% of submissions
    """
    merged_df = employees.merge(salaries, how="outer")
    return merged_df[merged_df.isnull().any(axis=1)][["employee_id"]]
