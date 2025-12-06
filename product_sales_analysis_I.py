import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Analyzes sales data by merging sales and product information.

    Tables:
        - Sales:
            | sale_id  | product_id | year | quantity | price |
            |   int    |     int    | int  |   int    | int   |
            (sale_id, year) is the primary key.
            product_id is a foreign key referencing Product.
            'price' is the per-unit price for the product sold.

        - Product:
            Contains 'product_id' and 'product_name'.

    Args:
        sales (pd.DataFrame): DataFrame with sales records.
        product (pd.DataFrame): DataFrame with product details.

    Returns:
        pd.DataFrame: DataFrame containing 'product_name', 'year', and 'price' for each sale.

    Example:
        Input:
            sales =
                sale_id  product_id  year  quantity  price
                1        100         2020  5         20
                2        101         2020  3         15
            product =
                product_id  product_name
                100         Apple
                101         Banana

        Output:
            product_name  year  price
            Apple         2020  20
            Banana        2020  15

    Time Complexity: O(N), where N is the number of sales records (merge and column operations are linear).
    Space Complexity: O(N), due to the merged output DataFrame.

    LeetCode: Beats 98.94% of submissions
    """
    merged = pd.merge(sales, product, on="product_id", how="left")
    merged = merged.drop(["sale_id", "quantity"], axis=1)
    return merged[["product_name", "year", "price"]]
