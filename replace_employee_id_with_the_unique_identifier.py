import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    """
    Replaces employee 'id' with a 'unique_id' for each employee where available.

    For each employee, display their 'name' and corresponding 'unique_id'.
    If an employee does not have a matching unique_id, display null for that entry.

    Args:
        employees (pd.DataFrame): Contains columns:
            - id (int): Employee's ID (primary key)
            - name (str): Employee's name

        employee_uni (pd.DataFrame): Contains columns:
            - id (int): Employee's ID (matches 'employees.id')
            - unique_id (int): The unique identifier for the employee

    Returns:
        pd.DataFrame: A DataFrame with columns ['name', 'unique_id'],
                      matching each employee's name to their unique_id if
                      available, or null otherwise.

    Example:
        employees =
            id  name
            1   Alice
            2   Bob

        employee_uni =
            id  unique_id
            1   101

        Output =
            name   unique_id
            Alice  101
            Bob    NaN

    Time Complexity: O(N), where N is the number of employees.
    Space Complexity: O(N).

    LeetCode: Beats 95.14% of submissions
    """
    return employees.merge(employee_uni, how="left").drop("id", axis=1)
