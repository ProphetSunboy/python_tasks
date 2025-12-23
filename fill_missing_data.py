import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    Fills missing values in the 'quantity' column of the given products
    DataFrame with 0.

    DataFrame Structure:
    +-------------+--------+
    | Column Name | Type   |
    +-------------+--------+
    | name        | object |
    | quantity    | int    |
    | price       | int    |
    +-------------+--------+

    Args:
        products (pd.DataFrame): Input DataFrame containing product data.

    Returns:
        pd.DataFrame: DataFrame with missing quantity values filled as 0.

    Example:
        Input:
            name   quantity  price
        0  apple     10      1
        1  orange    NaN     2
        Output:
            name   quantity  price
        0  apple     10      1
        1  orange     0      2

    Time Complexity: O(n), where n is the number of rows in the DataFrame.
    Space Complexity: O(1).

    LeetCode: Beats 94.15% of submissions
    """
    products["quantity"] = products["quantity"].fillna(0)
    return products
