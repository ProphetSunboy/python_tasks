import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the special bonus for each employee based on the following rules:

    - The 'Employees' table has the following columns:
        - employee_id (int): Unique identifier for each employee (primary key).
        - name (str): Employee's name.
        - salary (int): Employee's salary.

    The bonus for an employee is 100% of their salary if:
        - The employee_id is an odd number, and
        - The employee's name does not start with the character 'M'.

    Otherwise, the bonus is 0.

    Returns a DataFrame with columns:
        - employee_id: int
        - bonus: int

    The result is ordered by employee_id in ascending order.

    Example:
        Input:
        Employees table:
        +-------------+---------+--------+
        | employee_id | name    | salary |
        +-------------+---------+--------+
        | 2           | Meir    | 3000   |
        | 3           | Michael | 3800   |
        | 7           | Addilyn | 7400   |
        | 8           | Juan    | 6100   |
        | 9           | Kannon  | 7700   |
        +-------------+---------+--------+
        Output:
        +-------------+-------+
        | employee_id | bonus |
        +-------------+-------+
        | 2           | 0     |
        | 3           | 0     |
        | 7           | 7400  |
        | 8           | 0     |
        | 9           | 7700  |
        +-------------+-------+

    Time Complexity: O(n), where n is the number of employees.
    Space Complexity: O(1), excluding input and output DataFrames.

    LeetCode: Beats 93.05% of submissions
    """
    employees["bonus"] = 0
    bonus_ids = employees.loc[
        (employees["employee_id"] % 2 == 1) & ~(employees["name"].str.startswith("M"))
    ].index.tolist()
    employees.loc[bonus_ids, "bonus"] = employees.loc[bonus_ids, "salary"]

    return employees[["employee_id", "bonus"]].sort_values(by="employee_id")
