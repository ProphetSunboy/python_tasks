import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame 'employee' with the following schema:

        +-------------+---------+
        | Column Name | Type    |
        +-------------+---------+
        | id          | int     |  # Unique identifier for the employee
        | name        | varchar |  # Name of the employee
        | salary      | int     |  # Salary of the employee
        | managerId   | int     |  # ID of the manager (can be null)
        +-------------+---------+

    This function finds all employees who earn strictly more than their managers.

    Args:
        employee (pd.DataFrame): DataFrame containing employee data with
        columns ['id', 'name', 'salary', 'managerId'].

    Returns:
        pd.DataFrame: DataFrame with a single column 'Employee' listing the
        names of employees who earn more than their managers.

    Example:
        Input:
            id | name  | salary  | managerId
            -- | ----- | ------  | ---------
             1 | Alice | 70000   |   null
             2 | Bob   | 90000   |     1
             3 | Carol | 60000   |     1
             4 | Dave  | 100000  |     2

        Output:
             Employee
            ---------
            Bob
            Dave

    Time Complexity: O(n), where n is the number of employees (for the merge operation).
    Space Complexity: O(n), due to additional DataFrame for the merge.

    LeetCode: Beats 92.16% of submissions
    """
    empl = employee[~employee["managerId"].isnull()]
    merged = empl.merge(employee, how="left", left_on="managerId", right_on="id")
    return merged[merged["salary_x"] > merged["salary_y"]][["name_x"]].rename(
        columns={"name_x": "Employee"}
    )
