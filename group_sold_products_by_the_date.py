import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame 'activities' with the following schema:

        +-------------+---------+
        | Column Name | Type    |
        +-------------+---------+
        | sell_date   | date    |
        | product     | varchar |
        +-------------+---------+

    Each row represents a product sold on a specific date.
    The table may contain duplicates.

    This function returns, for each date, the number of unique products sold and a
    comma-separated, lexicographically sorted list of product names sold on that date.

    Args:
        activities (pd.DataFrame): DataFrame containing at least two columns:
            - 'sell_date': The date when a product was sold.
            - 'product': The name of the product sold.

    Returns:
        pd.DataFrame: A DataFrame with the following columns:
            - 'sell_date': The date of sale.
            - 'num_sold' : The number of unique products sold on that date.
            - 'products' : Comma-separated product names (sorted lexicographically) sold on that date.

    Example:
        Input DataFrame:
            sell_date  product
            2020-01-01 Banana
            2020-01-01 Apple
            2020-01-01 Banana
            2020-01-02 Apple

        Output DataFrame:
            sell_date    num_sold  products
            2020-01-01   2         Apple,Banana
            2020-01-02   1         Apple

    Time Complexity: O(M), where M is the number of rows in the DataFrame (due to grouping and aggregation).
    Space Complexity: O(M), since intermediate objects may store up to M unique rows.

    LeetCode: Beats 92.25% of submissions
    """
    activities_sorted = activities.drop_duplicates().sort_values("product")

    return (
        activities_sorted.groupby("sell_date")["product"]
        .agg(num_sold="nunique", products=lambda x: ",".join(x))
        .reset_index()
    )
