import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame `users` with columns:
        - user_id (int): unique identifier, primary key
        - name (str): user name containing only alphabetic characters
        (upper or lower case)

    Fix the names so that only the first letter is uppercase and the rest are
    lowercase (i.e., capitalize each name).

    Args:
        users (pd.DataFrame): DataFrame containing user_id and name.

    Returns:
        pd.DataFrame: DataFrame with corrected name capitalization, sorted by
        user_id.

    Example:
        Input:
            +---------+----------+
            | user_id | name     |
            +---------+----------+
            | 1       | aLEx     |
            | 2       | BOB      |
            | 3       | Alice    |
            +---------+----------+

        Output:
            +---------+-------+
            | user_id | name  |
            +---------+-------+
            | 1       | Alex  |
            | 2       | Bob   |
            | 3       | Alice |
            +---------+-------+

    Time Complexity: O(n), where n is the number of rows in users.
    Space Complexity: O(1) (modifies in-place except for the final sort).

    LeetCode: Beats 98.69% of submissions
    """
    users["name"] = users["name"].str.capitalize()

    return users.sort_values(by="user_id")
