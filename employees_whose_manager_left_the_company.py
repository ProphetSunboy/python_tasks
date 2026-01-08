import pandas as pd


def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame `employees` containing employee information, return the IDs
    of employees whose salary is strictly less than $30,000 and whose manager has
    left the company. When a manager leaves, their row is removed from the DataFrame,
    but their reports retain the manager_id.

    The result should be a DataFrame ordered by employee_id in ascending order.

    The input DataFrame has the following columns:
        - employee_id (int): The primary key, unique for each employee.
        - name (str): The name of the employee.
        - manager_id (int or None): The ID of the manager (can be None).
        - salary (int): The employee's salary.

    Args:
        employees (pd.DataFrame): A DataFrame containing employee information.

    Returns:
        pd.DataFrame: A DataFrame with a single column 'employee_id' for employees
            matching the given criteria, sorted by 'employee_id' in ascending order.

    Example:
        Input:
        Employees table:
        +-------------+-----------+------------+--------+
        | employee_id | name      | manager_id | salary |
        +-------------+-----------+------------+--------+
        | 3           | Mila      | 9          | 60301  |
        | 12          | Antonella | null       | 31000  |
        | 13          | Emery     | null       | 67084  |
        | 1           | Kalel     | 11         | 21241  |
        | 9           | Mikaela   | null       | 50937  |
        | 11          | Joziah    | 6          | 28485  |
        +-------------+-----------+------------+--------+
        Output:
        +-------------+
        | employee_id |
        +-------------+
        | 11          |
        +-------------+

    Time Complexity: O(n), where n is the number of employees.
    Space Complexity: O(1), excluding the space required for the output DataFrame.
    """
    return (
        employees[
            (employees["salary"] < 30_000)
            & ~(employees["manager_id"].isin(employees["employee_id"]))
        ]
        .dropna()[["employee_id"]]
        .sort_values(by="employee_id")
    )
