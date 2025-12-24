import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the names of customers who never placed any orders.

    Args:
        customers (pd.DataFrame): DataFrame with columns:
            - id (int): Unique customer ID (primary key)
            - name (str): Customer name
        orders (pd.DataFrame): DataFrame with columns:
            - id (int): Unique order ID (primary key)
            - customerId (int): Customer ID who placed the order (foreign key to customers.id)

    Returns:
        pd.DataFrame: DataFrame with a single column "Customers" containing the
        names of customers who have never placed an order.

    Example:
        customers = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob']})
        orders = pd.DataFrame({'id': [1], 'customerId': [2]})

        Output:
            Customers
        0     Alice

    Time Complexity: O(m + n), where m = number of customers, n = number of orders.
    Space Complexity: O(m)

    LeetCode: Beats 93.86% of submissions
    """
    merged_df = customers.merge(orders, how="left", left_on="id", right_on="customerId")
    return merged_df[merged_df["id_y"].isnull()][["name"]].rename(
        columns={"name": "Customers"}
    )
