import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the customer_number of the customer who placed the largest number of orders.

    The `orders` DataFrame must have the following columns:
        - order_number: int, unique identifier for each order (primary key)
        - customer_number: int, identifier for the customer who placed the order

    Args:
        orders (pd.DataFrame): DataFrame containing order_number and customer_number.

    Returns:
        pd.DataFrame: A DataFrame containing a single column 'customer_number' with the customer number
                      that have the highest order counts.

    Example:
        Input:
            orders = pd.DataFrame({
                'order_number': [1, 2, 3, 4],
                'customer_number': [1, 2, 2, 3]
            })
        Output:
            customer_number
            0             2

    Time Complexity: O(n), where n is the number of rows in the orders DataFrame.
    Space Complexity: O(k), where k is the number of unique customer_numbers.

    LeetCode: Beats 92.67% of submissions
    """
    most_freq = orders.value_counts(subset="customer_number").idxmax()
    return pd.DataFrame([most_freq], columns=["customer_number"])
