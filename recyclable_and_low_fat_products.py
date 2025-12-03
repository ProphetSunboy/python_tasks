import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame `products` with the following columns:
        - product_id (int): Primary key, unique identifier for each product.
        - low_fats (str): 'Y' if the product is low fat, 'N' otherwise.
        - recyclable (str): 'Y' if the product is recyclable, 'N' otherwise.

    This function finds all products that are BOTH low fat AND recyclable.

    Args:
        products (pd.DataFrame): DataFrame containing columns
            'product_id', 'low_fats', and 'recyclable'.

    Returns:
        pd.DataFrame: DataFrame with a single column 'product_id' listing products
        that are both low fat and recyclable.

    Example:
        Input:
            products =
               product_id low_fats recyclable
            0          1        Y          Y
            1          2        Y          N
            2          3        N          Y
            3          4        Y          Y

        Output:
           product_id
        0           1
        1           4

    Time Complexity: O(N), where N is the number of products.
    Space Complexity: O(N).

    LeetCode: Beats 92.80% of submissions
    """
    return products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")][
        ["product_id"]
    ]
