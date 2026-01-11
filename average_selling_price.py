import pandas as pd
import numpy as np


def average_selling_price(
    prices: pd.DataFrame, units_sold: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate the average selling price for each product.

    Parameters:
        prices (pd.DataFrame): DataFrame containing product pricing periods with columns:
            - product_id (int): ID of the product
            - start_date (date): Start date of the pricing period
            - end_date (date): End date of the pricing period
            - price (int): Price during the period
            Each (product_id, start_date, end_date) tuple is unique and periods do not overlap per product.

        units_sold (pd.DataFrame): DataFrame containing sales transactions with columns:
            - product_id (int): ID of the product
            - purchase_date (date): Date of sale
            - units (int): Units sold
            Rows may be duplicated.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - product_id (int): ID of the product
            - average_price (float): Average selling price per unit, rounded to 2 decimals.
              If a product has no sold units, average_price is 0.00.

    Example:
        Input:
        Prices table:
        +------------+------------+------------+--------+
        | product_id | start_date | end_date   | price  |
        +------------+------------+------------+--------+
        | 1          | 2019-02-17 | 2019-02-28 | 5      |
        | 1          | 2019-03-01 | 2019-03-22 | 20     |
        | 2          | 2019-02-01 | 2019-02-20 | 15     |
        | 2          | 2019-02-21 | 2019-03-31 | 30     |
        +------------+------------+------------+--------+
        UnitsSold table:
        +------------+---------------+-------+
        | product_id | purchase_date | units |
        +------------+---------------+-------+
        | 1          | 2019-02-25    | 100   |
        | 1          | 2019-03-01    | 15    |
        | 2          | 2019-02-10    | 200   |
        | 2          | 2019-03-22    | 30    |
        +------------+---------------+-------+
        Output:
        +------------+---------------+
        | product_id | average_price |
        +------------+---------------+
        | 1          | 6.96          |
        | 2          | 16.96         |
        +------------+---------------+

    Time Complexity: O(n), where n is the number of digits.
    Space Complexity: O(1), aside from the input and output lists.

    LeetCode: Beats 96.67% of submissions
    """
    df = pd.merge(prices, units_sold, on="product_id", how="left")

    valid_sales = (df["purchase_date"] >= df["start_date"]) & (
        df["purchase_date"] <= df["end_date"]
    )
    df["units"] = np.where(valid_sales, df["units"], 0)

    df["revenue"] = df["price"] * df["units"]

    res = df.groupby("product_id").agg({"revenue": "sum", "units": "sum"}).reset_index()

    res["average_price"] = np.where(
        res["units"] > 0, (res["revenue"] / res["units"]).round(2), 0.00
    )

    return res[["product_id", "average_price"]]
