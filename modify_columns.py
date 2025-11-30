import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Modifies the salary column of the given DataFrame by doubling each
    employee's salary.

    Args:
        employees (pd.DataFrame): A DataFrame with the following columns:
            - name (object): The employee's name.
            - salary (int): The employee's salary.

    Returns:
        pd.DataFrame: The DataFrame with the updated salary column.

    Example:
        Input:
           name  salary
        0  John   1000
        1  Jane   1200

        Output:
           name  salary
        0  John   2000
        1  Jane   2400

    Time: O(n) - One operation per row in the DataFrame.
    Space: O(n) - Returns a DataFrame of the same size.

    LeetCode: Beats 91.09% of submissions
    """
    employees["salary"] = employees["salary"] * 2

    return employees
