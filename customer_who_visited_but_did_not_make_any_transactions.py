import pandas as pd


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Finds customers who visited the mall but did not make any transactions,
    and counts how many such visits each customer made.

    Args:
        visits (pd.DataFrame): DataFrame with columns:
            - visit_id (int, unique): ID of the visit.
            - customer_id (int): ID of the customer who visited.
        transactions (pd.DataFrame): DataFrame with columns:
            - transaction_id (int, unique): ID of the transaction.
            - visit_id (int): ID of the visit during which the transaction was made.
            - amount (int): The amount spent in the transaction.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - customer_id (int): ID of the customer who visited without making transactions.
            - count_no_trans (int): Number of visits made by the customer without any transactions.

    Time Complexity: O(n log n), primarily from groupby operations.
    Space Complexity: O(1), not counting input storage.

    LeetCode: Beats 91.29% of submissions
    """
    merged_df = visits.merge(transactions, how="left", on="visit_id").drop(
        ["amount", "visit_id"], axis=1
    )
    without_trans = merged_df[merged_df["transaction_id"].isnull()]
    return (
        without_trans.groupby("customer_id")
        .size()
        .reset_index()
        .rename(columns={0: "count_no_trans"})
    )
