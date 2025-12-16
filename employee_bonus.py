import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with the name and bonus amount of each employee who either:
        1. Has a bonus less than 1000, or
        2. Did not receive any bonus.

    Args:
        employee (pd.DataFrame): DataFrame with columns:
            - empId (int): Unique employee ID
            - name (str): Employee name
            - supervisor (int): Supervisor ID
            - salary (int): Employee salary

        bonus (pd.DataFrame): DataFrame with columns:
            - empId (int): Employee ID (foreign key to employee.empId)
            - bonus (int): Bonus amount

    Returns:
        pd.DataFrame: DataFrame with columns:
            - name (str): Employee name
            - bonus (float or NaN): Bonus amount (NaN if no bonus)

    Example:
        Input:
            employee =
            | empId | name   | supervisor | salary |
            |-------|--------|------------|--------|
            | 1     | John   | 3          | 1000   |
            | 2     | Jane   | 3          | 1500   |
            | 3     | Alice  | 0          | 5000   |
            bonus =
            | empId | bonus  |
            |-------|--------|
            | 2     | 800    |
            | 3     | 1500   |

        Output:
            | name  | bonus |
            |-------|-------|
            | John  | NaN   |
            | Jane  | 800   |

    Time Complexity: O(N), where N is the number of employees.
    Space Complexity: O(N), output DataFrame size.

    LeetCode: Beats 95.69% of submissions
    """
    merged_df = employee.merge(bonus, how="left")
    return merged_df[(merged_df["bonus"] < 1000) | (merged_df["bonus"].isna())][
        ["name", "bonus"]
    ]
