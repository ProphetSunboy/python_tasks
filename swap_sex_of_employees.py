import pandas as pd


def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    """
    Swaps the values of the 'sex' column in the Salary DataFrame.

    The 'sex' column is an ENUM type containing the values 'm' and 'f'.
    After execution, all 'm' values will be changed to 'f', and all 'f' values
    will be changed to 'm'.

    Args:
        salary (pd.DataFrame): DataFrame with at least the columns 'id', 'name',
        'sex', and 'salary'.

    Returns:
        pd.DataFrame: The same DataFrame with swapped 'sex' values.

    Example:
        Input:
            id | name  | sex | salary
            --------------------------
            1  | Alice | f   | 1200
            2  | Bob   | m   | 1500

        Output:
            id | name  | sex | salary
            --------------------------
            1  | Alice | m   | 1200
            2  | Bob   | f   | 1500

    Time Complexity: O(N), where N is the number of rows in the DataFrame.
    Space Complexity: O(1), as the replacement is done in-place (excluding DataFrame storage).

    LeetCode: Beats 91.32% of submissions
    """
    salary["sex"] = salary["sex"].replace({"f": "m", "m": "f"})

    return salary
