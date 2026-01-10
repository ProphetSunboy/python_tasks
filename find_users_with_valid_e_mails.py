import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """
    Returns users with valid email addresses according to specified rules.

    A valid email must:
      - Begin with a prefix starting with a letter (a-z or A-Z) and can contain
      letters, digits, underscores '_', periods '.', and dashes '-'.
      - Use the domain '@leetcode.com' (case-sensitive and exact match).

    Args:
        users : pd.DataFrame
            DataFrame containing user data with the following columns:
            - user_id (int): Unique identifier for the user.
            - name (str): Name of the user.
            - mail (str): E-mail address of the user.

    Returns:
        pd.DataFrame: DataFrame containing all columns for users whose 'mail'
        columns are valid per the rules above.

    Example
        Input:
        Users table:
        +---------+-----------+-------------------------+
        | user_id | name      | mail                    |
        +---------+-----------+-------------------------+
        | 1       | Winston   | winston@leetcode.com    |
        | 2       | Jonathan  | jonathanisgreat         |
        | 3       | Annabelle | bella-@leetcode.com     |
        | 4       | Sally     | sally.come@leetcode.com |
        | 5       | Marwan    | quarz#2020@leetcode.com |
        | 6       | David     | david69@gmail.com       |
        | 7       | Shapiro   | .shapo@leetcode.com     |
        +---------+-----------+-------------------------+
        Output:
        +---------+-----------+-------------------------+
        | user_id | name      | mail                    |
        +---------+-----------+-------------------------+
        | 1       | Winston   | winston@leetcode.com    |
        | 3       | Annabelle | bella-@leetcode.com     |
        | 4       | Sally     | sally.come@leetcode.com |
        +---------+-----------+-------------------------+

    Time Complexity: O(n), where n is the number of users.
    Space Complexity: O(1), not including the output DataFrame.

    LeetCode: Beats 94.41% of submissions
    """
    return users[users["mail"].str.match("^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$")]
