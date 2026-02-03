import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the capital gain/loss for each stock based on buy and sell operations.

    Table: Stocks

        +---------------+---------+
        | Column Name   | Type    |
        +---------------+---------+
        | stock_name    | varchar |
        | operation     | enum    |
        | operation_day | int     |
        | price         | int     |
        +---------------+---------+

    (stock_name, operation_day) is the primary key.
    The operation column is an ENUM of type ('Sell', 'Buy').
    Each row indicates that the stock (stock_name) had an operation on operation_day at the given price.
    Every 'Sell' operation has a corresponding 'Buy' on a previous day, and vice versa.

    The capital gain/loss of a stock is the total gain or loss after buying and
    selling the stock one or more times.

    Args:
        stocks (pd.DataFrame): A DataFrame with the stock data.

    Returns:
        pd.DataFrame: A DataFrame with each stock_name and its corresponding
        capital gain or loss.

    Example:
        Input:
        Stocks table:
        +---------------+-----------+---------------+--------+
        | stock_name    | operation | operation_day | price  |
        +---------------+-----------+---------------+--------+
        | Leetcode      | Buy       | 1             | 1000   |
        | Corona Masks  | Buy       | 2             | 10     |
        | Leetcode      | Sell      | 5             | 9000   |
        | Handbags      | Buy       | 17            | 30000  |
        | Corona Masks  | Sell      | 3             | 1010   |
        | Corona Masks  | Buy       | 4             | 1000   |
        | Corona Masks  | Sell      | 5             | 500    |
        | Corona Masks  | Buy       | 6             | 1000   |
        | Handbags      | Sell      | 29            | 7000   |
        | Corona Masks  | Sell      | 10            | 10000  |
        +---------------+-----------+---------------+--------+
        Output:
        +---------------+-------------------+
        | stock_name    | capital_gain_loss |
        +---------------+-------------------+
        | Corona Masks  | 9500              |
        | Leetcode      | 8000              |
        | Handbags      | -23000            |
        +---------------+-------------------+

    Time Complexity: O(n), where n is the number of stock operations (rows).
    Space Complexity: O(k), where k is the number of unique stock names.

    LeetCode: Beats 94.50% of submissions
    """
    stocks.loc[stocks["operation"] == "Buy", "price"] *= -1

    return (
        stocks.groupby("stock_name")["price"]
        .sum()
        .reset_index()
        .rename(columns={"price": "capital_gain_loss"})
    )
