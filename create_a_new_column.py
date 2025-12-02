import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame 'employees' with the following columns:
        - name (object): The employee's name.
        - salary (int): The employee's salary.

    This function adds a new column 'bonus' to the DataFrame, where 'bonus' is
    computed as double the value in the 'salary' column for each employee.

    Args:
        employees (pd.DataFrame): DataFrame containing columns 'name' and 'salary'.

    Returns:
        pd.DataFrame: The original DataFrame with an added 'bonus' column.

    Example:
        Input:
            name   salary
        0  Alice   1000
        1    Bob   1500

        Output:
            name   salary  bonus
        0  Alice   1000    2000
        1    Bob   1500    3000

    Time Complexity: O(n), where n is the number of employees.
    Space Complexity: O(1), not including the output DataFrame.

    LeetCode: Beats 93.98% of submissions
    """
    employees["bonus"] = employees["salary"] * 2
    return employees
