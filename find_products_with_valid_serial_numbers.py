import pandas as pd


def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Find products whose description contains a valid serial number.

    A valid serial number must match the following pattern:
        - Starts with the letters 'SN' (case-sensitive)
        - Followed by exactly 4 digits
        - Followed by a hyphen '-'
        - Followed by exactly 4 digits
    The serial number can appear anywhere within the description.

    Args:
        products (pd.DataFrame): DataFrame with columns:
            - product_id (int): Unique product ID
            - product_name (str): Name of the product
            - description (str): Product description

    Returns:
        pd.DataFrame: Filtered DataFrame of products whose description contains
                      a valid serial number, sorted by product_id

    Example:
        Input:

        products table:

        +------------+--------------+------------------------------------------------------+
        | product_id | product_name | description                                          |
        +------------+--------------+------------------------------------------------------+
        | 1          | Widget A     | This is a sample product with SN1234-5678            |
        | 2          | Widget B     | A product with serial SN9876-1234 in the description |
        | 3          | Widget C     | Product SN1234-56789 is available now                |
        | 4          | Widget D     | No serial number here                                |
        | 5          | Widget E     | Check out SN4321-8765 in this description            |
        +------------+--------------+------------------------------------------------------+

        Output:

        +------------+--------------+------------------------------------------------------+
        | product_id | product_name | description                                          |
        +------------+--------------+------------------------------------------------------+
        | 1          | Widget A     | This is a sample product with SN1234-5678            |
        | 2          | Widget B     | A product with serial SN9876-1234 in the description |
        | 5          | Widget E     | Check out SN4321-8765 in this description            |
        +------------+--------------+------------------------------------------------------+

    Time Complexity: O(m), where m is the total number of characters in the 'description' column.
    Space Complexity: O(1), not counting input and output storage.

    LeetCode: Beats 94.12% of submissions
    """
    return products[
        products["description"].str.contains(r"\bSN\d{4}-\d{4}\b")
    ].sort_values(by="product_id")
