import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the products that were only sold in the first quarter of 2019,
    i.e., between 2019-01-01 and 2019-03-31 inclusive.

    Tables:
        Product:
            - product_id (int): Primary key, unique product identifier.
            - product_name (str): Name of the product.
            - unit_price (int): Price per unit.

        Sales:
            - seller_id (int)
            - product_id (int): Foreign key to Product table.
            - buyer_id (int)
            - sale_date (date)
            - quantity (int)
            - price (int)

    Args:
        product (pd.DataFrame): DataFrame containing product information.
        sales (pd.DataFrame): DataFrame containing sales records.

    Returns:
        pd.DataFrame: DataFrame with the products only sold between
            2019-01-01 and 2019-03-31 (inclusive).

    Example:
        Input:
        Product table:
        +------------+--------------+------------+
        | product_id | product_name | unit_price |
        +------------+--------------+------------+
        | 1          | S8           | 1000       |
        | 2          | G4           | 800        |
        | 3          | iPhone       | 1400       |
        +------------+--------------+------------+
        Sales table:
        +-----------+------------+----------+------------+----------+-------+
        | seller_id | product_id | buyer_id | sale_date  | quantity | price |
        +-----------+------------+----------+------------+----------+-------+
        | 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
        | 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
        | 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
        | 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
        +-----------+------------+----------+------------+----------+-------+
        Output:
        +-------------+--------------+
        | product_id  | product_name |
        +-------------+--------------+
        | 1           | S8           |
        +-------------+--------------+

    Time Complexity: O(m), where m is the number of sales records.
    Space Complexity: O(p), where p is the number of products returned.
    """
    merged = sales.merge(product, how="left")

    grouped = (
        merged.groupby(["product_id", "product_name"])["sale_date"]
        .apply(lambda x: (x.between("2019-01-01", "2019-03-31")).all())
        .reset_index()
    )

    return grouped[grouped["sale_date"]].drop("sale_date", axis=1)
