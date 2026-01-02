import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    """
    Given two DataFrames:
        - users: Contains user information with columns:
            - user_id (int): Unique identifier for each user (primary key)
            - user_name (str): Name of the user

        - register: Contains contest registration info with columns:
            - contest_id (int): Contest identifier
            - user_id (int): User identifier
            (contest_id, user_id) forms the primary key

    This function calculates the percentage of total users who registered for
    each contest, rounding the result to two decimal places.

    Args:
        users (pd.DataFrame): DataFrame containing user information.
        register (pd.DataFrame): DataFrame containing contest registration info.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - contest_id (int)
            - percentage (float): Percentage of users registered to each contest,
              rounded to two decimals.
        The result is ordered by percentage in descending order. In case of a tie,
        contests with the same percentage are sorted by contest_id in ascending order.

    Example:
        Input:
        Users table:
        +---------+-----------+
        | user_id | user_name |
        +---------+-----------+
        | 6       | Alice     |
        | 2       | Bob       |
        | 7       | Alex      |
        +---------+-----------+
        Register table:
        +------------+---------+
        | contest_id | user_id |
        +------------+---------+
        | 215        | 6       |
        | 209        | 2       |
        | 208        | 2       |
        | 210        | 6       |
        | 208        | 6       |
        | 209        | 7       |
        | 209        | 6       |
        | 215        | 7       |
        | 208        | 7       |
        | 210        | 2       |
        | 207        | 2       |
        | 210        | 7       |
        +------------+---------+
        Output:
        +------------+------------+
        | contest_id | percentage |
        +------------+------------+
        | 208        | 100.0      |
        | 209        | 100.0      |
        | 210        | 100.0      |
        | 215        | 66.67      |
        | 207        | 33.33      |
        +------------+------------+

    Time Complexity: O(n), where n is the number of registrations.
    Space Complexity: O(k), where k is the number of contests.

    LeetCode: Beats 98.68% of submissions
    """
    grouped_df = (
        register.groupby("contest_id")
        .size()
        .reset_index()
        .rename(columns={0: "percentage"})
    )
    grouped_df["percentage"] = (grouped_df["percentage"] / len(users) * 100).round(
        decimals=2
    )

    return grouped_df.sort_values(
        by=["percentage", "contest_id"], ascending=[False, True]
    )
