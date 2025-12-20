import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame 'employee' with columns:
        - employee_id (int): Employee's ID.
        - department_id (int): Department's ID.
        - primary_flag (str): 'Y' if this is the employee's primary department, 'N' otherwise.
      (employee_id, department_id) together are unique.

    Employees may belong to multiple departments. If so, only one row will have
    'primary_flag'='Y' (the primary department) per employee.
    If an employee belongs to only one department, then 'primary_flag' is always
    'N' for that row.

    This function returns a DataFrame listing each employee's primary department:
        - For employees in multiple departments, select the department where 'primary_flag'='Y'.
        - For employees in only one department, select that department (even if 'primary_flag'='N').

    Args:
        employee (pd.DataFrame): DataFrame with columns ['employee_id', 'department_id', 'primary_flag'].

    Returns:
        pd.DataFrame: DataFrame with columns ['employee_id', 'department_id'], listing each employee's primary department.

    Example:
        Input:
            employee_id | department_id | primary_flag
            ------------|---------------|-------------
            1           | 10            | N
            1           | 20            | Y
            2           | 30            | N
        Output:
            employee_id | department_id
            ------------|--------------
            1           | 20
            2           | 30
        Explanation:
            - For employee 1, two departments: department_id 20 is primary ('Y').
            - For employee 2, only one department. Despite primary_flag being 'N',
            that is their only and thus primary department.

    Time Complexity: O(N)
    Space Complexity: O(N)

    LeetCode: Beats 95.11% of submissions
    """
    return employee[
        (employee["primary_flag"] == "Y")
        | ~(employee.duplicated(subset=["employee_id"], keep=False))
    ][["employee_id", "department_id"]]
