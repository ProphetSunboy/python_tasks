import pandas as pd


def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    Given two DataFrames, `products` and `orders`, return a DataFrame containing
    the names of products that have a total of at least 100 units ordered during
    February 2020, along with the total units ordered for each product.

    Args:
        products (pd.DataFrame): DataFrame containing product information with the following columns:
            - product_id (int): Primary key of the product.
            - product_name (str): Name of the product.
            - product_category (str): Category of the product.
        orders (pd.DataFrame): DataFrame containing order transactions with the following columns:
            - product_id (int): References products.product_id.
            - order_date (datetime or date): Date of the order.
            - unit (int): Number of units ordered.

    Returns:
        pd.DataFrame: DataFrame with columns ["product_name", "unit"], for
        products with at least 100 units ordered in February 2020.

    Example:
        products = pd.DataFrame({
            'product_id': [1, 2],
            'product_name': ['Apple', 'Banana'],
            'product_category': ['Fruit', 'Fruit']
        })
        orders = pd.DataFrame({
            'product_id': [1, 2, 1, 2],
            'order_date': pd.to_datetime(['2020-02-05', '2020-02-07', '2020-01-15', '2020-02-20']),
            'unit': [40, 120, 90, 30]
        })

        Output:
            product_name  unit
        0       Banana    150

    Time Complexity: O(m + k), where m is the number of orders and k is the number of products.
    Space Complexity: O(k), due to grouping and merging operations.

    LeetCode: Beats 90.34% of submissions
    """
    df = products.merge(
        orders[
            (orders["order_date"].dt.year == 2020)
            & (orders["order_date"].dt.month == 2)
        ]
        .groupby("product_id")[["unit"]]
        .sum()
        .reset_index(),
        how="inner",
    )
    return df[df["unit"] >= 100][["product_name", "unit"]]
