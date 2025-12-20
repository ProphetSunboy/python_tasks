import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame representing a Person table:

        +-------------+---------+
        | Column Name | Type    |
        +-------------+---------+
        | id          | int     |
        | email       | varchar |
        +-------------+---------+
        id is the primary key (unique for each row).
        The email column contains only lowercase letters and is guaranteed not
        to be NULL.

    The task is to return all duplicate email addresses in the table.
    The result should be a DataFrame with a single column 'Email' containing
    emails that appear more than once, with no duplicates in the result.

    Args:
        person (pd.DataFrame): DataFrame with columns 'id' and 'email'.

    Returns:
        pd.DataFrame: DataFrame with a single column 'Email' listing duplicate
        email addresses (each only once).

    Example:
        Input:
            id | email
           ---|------------
            1  | a@b.com
            2  | c@d.com
            3  | a@b.com
        Output:
            Email
            -------
            a@b.com

    Time Complexity: O(N), where N is the number of rows in the input DataFrame.
    Space Complexity: O(N).

    LeetCode: Beats 92.21% of submissions
    """
    return (
        person[person["email"].duplicated(keep=False)][["email"]]
        .rename(columns={"email": "Email"})
        .drop_duplicates(subset=["Email"])
    )
