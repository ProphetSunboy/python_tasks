import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows from the DataFrame based on the 'email' column,
    keeping only the first occurrence of each email.

    Args:
        customers (pd.DataFrame): A DataFrame with the following columns:
            - customer_id (int)
            - name (object)
            - email (object)

    Returns:
        pd.DataFrame: A DataFrame with duplicate emails removed, retaining the
        first occurrence.

    Example:
        Input:
           customer_id   name       email
        0           1   Alice       a@a.com
        1           2     Bob       b@b.com
        2           3   Carol       a@a.com

        Output:
           customer_id   name       email
        0           1   Alice  a@a.com
        1           2     Bob  b@b.com

    Time Complexity: O(N), where N is the number of rows in the DataFrame.
    Space Complexity: O(N), due to the output DataFrame.

    LeetCode: Beats 97.31% of submissions
    """
    return customers.drop_duplicates(subset=["email"], keep="first")
