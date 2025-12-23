import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with the names of customers who are either:
        - Not referred by any customer (referee_id is null)
        - Referred by a customer whose id is not 2

    Table Schema:
        +-------------+---------+
        | Column Name | Type    |
        +-------------+---------+
        | id          | int     |  # Primary key
        | name        | varchar |
        | referee_id  | int     |
        +-------------+---------+

    Args:
        customer (pd.DataFrame): Input DataFrame representing the Customer table.
            Must contain columns ['id', 'name', 'referee_id'].

    Returns:
        pd.DataFrame: DataFrame with column ['name'] containing qualifying customer names.

    Example:
        Input:
            id  name     referee_id
        0   1   Will     None
        1   2   Jane     1
        2   3   Alex     2
        3   4   Bill     None
        Output:
            name
        0   Will
        1   Jane
        3   Bill

    Time Complexity: O(n), where n is the number of customers.
    Space Complexity: O(1).

    LeetCode: Beats 94.92% of submissions
    """
    return customer[(customer["referee_id"] != 2) | (customer["referee_id"].isnull())][
        ["name"]
    ]
