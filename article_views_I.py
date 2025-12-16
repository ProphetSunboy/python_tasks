import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    """
    The function finds all unique authors who have viewed at least one of their
    own articles.
    Returns a DataFrame with a single column 'id', sorted in ascending order.

    There may be duplicate rows and no primary key in this table.

    Args:
        views (pd.DataFrame): DataFrame containing views data with columns
        'article_id', 'author_id', 'viewer_id', 'view_date'.

    Returns:
        pd.DataFrame: DataFrame with a single column 'id' listing unique author
        ids who have viewed at least one of their own articles, sorted in
        ascending order.

    Example:
        Input:
            views =
            | article_id | author_id | viewer_id | view_date  |
            |------------|-----------|-----------|------------|
            |     1      |     1     |     1     | 2024-06-01 |
            |     2      |     2     |     3     | 2024-06-01 |
            |     1      |     1     |     2     | 2024-06-02 |
            |     3      |     4     |     4     | 2024-06-02 |
        Output:
            | id |
            |----|
            |  1 |
            |  4 |

    Time Complexity: O(N), where N is the number of rows in the DataFrame.
    Space Complexity: O(K), where K is the number of unique authors satisfying the condition.

    LeetCode: Beats 95.78% of submissions
    """
    return (
        views[views["author_id"] == views["viewer_id"]][["author_id"]]
        .drop_duplicates()
        .rename(columns={"author_id": "id"})
        .sort_values(by="id")
    )
