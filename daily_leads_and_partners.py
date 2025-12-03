import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame `daily_sales` with columns:
        - date_id (date): The date of the sale.
        - make_name (str): The name of the product (lowercase).
        - lead_id (int): The lead's ID.
        - partner_id (int): The partner's ID.

    Each row records a sale. The table may have duplicates and does not have a
    primary key.

    For each combination of date_id and make_name, this function computes:
        - The number of unique lead_id values as 'unique_leads'.
        - The number of unique partner_id values as 'unique_partners'.

    Args:
        daily_sales (pd.DataFrame): DataFrame containing sales records with columns
                                    'date_id', 'make_name', 'lead_id', and 'partner_id'.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - date_id
            - make_name
            - unique_leads
            - unique_partners

    Example:
        Input:
            daily_sales =
               date_id   make_name  lead_id  partner_id
            0  2022-08-01      toyota        1           2
            1  2022-08-01      toyota        1           3
            2  2022-08-01      toyota        2           2
            3  2022-08-01      honda         1           4
            4  2022-08-02      toyota        2           2

        Output:
           date_id   make_name  unique_leads  unique_partners
        0  2022-08-01     honda             1                1
        1  2022-08-01     toyota            2                2
        2  2022-08-02     toyota            1                1

    Time Complexity: O(N), where N is the number of records in daily_sales.
    Space Complexity: O(N).

    LeetCode: Beats 96.57% of submissions
    """
    return (
        daily_sales.groupby(["date_id", "make_name"])
        .nunique()
        .reset_index()
        .rename(columns={"lead_id": "unique_leads", "partner_id": "unique_partners"})
    )
