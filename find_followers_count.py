import pandas as pd


def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    """
    Given a pandas DataFrame `followers` with columns:
        - user_id: int (the user being followed)
        - follower_id: int (a user who follows `user_id`)
    (user_id, follower_id) is the primary key.

    Returns a DataFrame with each user_id and their corresponding number of followers.

    Args:
        followers (pd.DataFrame): DataFrame containing columns "user_id" and "follower_id".

    Returns:
        pd.DataFrame: DataFrame with columns:
            - user_id: int
            - followers_count: int (the number of followers for each user)

    Example:
        Input:
            followers = pd.DataFrame({
                "user_id": [1, 2, 2, 3],
                "follower_id": [10, 10, 20, 30]
            })
        Output:
            pd.DataFrame({
                "user_id": [1, 2, 3],
                "followers_count": [1, 2, 1]
            })

    Time Complexity: O(n), where n is the number of rows in followers.
    Space Complexity: O(k), where k is the number of distinct user_ids.

    LeetCode: Beats 99.45% of submissions
    """
    return (
        followers.groupby("user_id")
        .count()
        .reset_index()
        .rename(columns={"follower_id": "followers_count"})
    )
