import pandas as pd


def queries_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Table: Queries

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | query_name  | varchar |
    | result      | varchar |
    | position    | int     |
    | rating      | int     |
    +-------------+---------+

    This table may have duplicate rows.
    The table contains information collected from some queries on a database.
    The position column has a value from 1 to 500.
    The rating column has a value from 1 to 5.
    A query with rating less than 3 is considered a poor query.

    Query quality is defined as the average of the ratio between query rating
    and its position.

    Poor query percentage is defined as the percentage of all queries with
    rating less than 3.

    Find each query_name, the quality, and poor_query_percentage.
    Both quality and poor_query_percentage should be rounded to 2 decimal places.

    Returns:
        pd.DataFrame: A DataFrame with columns ['query_name', 'quality', 'poor_query_percentage'].

    LeetCode: Beats 90.09% of submissions
    """
    df = df.assign(
        quality=df.rating / df.position + 1e-10,
        poor_query_percentage=(df.rating < 3).astype(int) * 100,
    )
    return (
        df.groupby("query_name", as_index=False)[["quality", "poor_query_percentage"]]
        .mean()
        .round(2)
    )
