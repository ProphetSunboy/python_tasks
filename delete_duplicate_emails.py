import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """
    Deletes duplicate emails from the provided DataFrame, keeping only the row
    with the smallest id for each unique email.
    Remove duplicates in place, keeping the lowest id per email.

    Args:
        person (pd.DataFrame): DataFrame with columns 'id' (int, unique) and
        'email' (str, lowercase only).

    Example:
        Input:
            id | email
        ----|----------
            1 | a@b.com
            2 | c@d.com
            3 | a@b.com

        Output:
            id | email
        ----|----------
            1 | a@b.com
            2 | c@d.com

    Time Complexity: O(n log n) for sorting.
    Space Complexity: O(1), in-place operation (excluding pandas internal overhead).

    LeetCode: Beats 96.87% of submissions
    """
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)
