import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    """
    Reformat the Department table so each row represents a department and each
    month's revenue is displayed in a separate column.

    Table: Department
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | revenue     | int     |
    | month       | varchar |
    +-------------+---------+
    (id, month) is the primary key.
    'month' takes its value from:
    ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
    Each row contains the revenue of a department for a specific month.

    Args:
        department (pd.DataFrame): DataFrame with columns:
            - id (int): Department id
            - revenue (int): Revenue for the department in that month
            - month (str): Month for which the revenue is recorded

    Returns:
        pd.DataFrame: Reformatted table with columns:
            - id (int): Department id
            - <Month>_Revenue (float or int): Revenue for each month from Jan to
            Dec as columns

    Example:
        Input:
            +------+---------+-------+
            | id   | revenue | month |
            +------+---------+-------+
            | 1    | 8000    | Jan   |
            | 2    | 9000    | Jan   |
            | 3    | 10000   | Feb   |
            | 1    | 7000    | Feb   |
            | 1    | 6000    | Mar   |
            +------+---------+-------+
        Output:
            +------+-------------+-------------+-------------+-----+-------------+
            | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
            +------+-------------+-------------+-------------+-----+-------------+
            | 1    | 8000        | 7000        | 6000        | ... | null        |
            | 2    | 9000        | null        | null        | ... | null        |
            | 3    | null        | 10000       | null        | ... | null        |
            +------+-------------+-------------+-------------+-----+-------------+

    Time Complexity: O(N)
    Space Complexity: O(D*M) where D = number of departments, M = number of months

    LeetCode: Beats 93.37% of submissions
    """
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    department = department.pivot(index="id", columns="month", values="revenue")

    return (
        department.reindex(columns=months, fill_value=np.nan)
        .add_suffix("_Revenue")
        .reset_index()
    )
