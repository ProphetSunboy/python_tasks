import pandas as pd


def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """
    Finds all valid email addresses in the provided DataFrame based on specific
    validation criteria.

    A valid email address must meet ALL of the following:
        - Contains exactly one '@' symbol.
        - Ends with '.com'.
        - The part before the '@' symbol contains only alphanumeric characters and underscores.
        - The domain (between '@' and '.com') contains only letters.

    The result is sorted by user_id in ascending order.

    Args:
        users (pd.DataFrame): DataFrame with columns 'user_id' and 'email'.

    Returns:
        pd.DataFrame: DataFrame of users with valid emails, ordered by user_id.

    Example:
        Input:
        Users table:
        +---------+---------------------+
        | user_id | email               |
        +---------+---------------------+
        | 1       | alice@example.com   |
        | 2       | bob_at_example.com  |
        | 3       | charlie@example.net |
        | 4       | david@domain.com    |
        | 5       | eve@invalid         |
        +---------+---------------------+
        Output:
        +---------+-------------------+
        | user_id | email             |
        +---------+-------------------+
        | 1       | alice@example.com |
        | 4       | david@domain.com  |
        +---------+-------------------+

    Time Complexity: O(m), where m is the number of rows in the DataFrame.
    Space Complexity: O(k), where k is the number of valid emails returned (output DataFrame).

    LeetCode: Beats 92.02% of submissions
    """
    regex = r"^[A-Za-z0-9_]+@[A-Za-z]+\.com$"

    mask = users["email"].str.match(regex, na=False)

    return users[mask].sort_values(by="user_id")
