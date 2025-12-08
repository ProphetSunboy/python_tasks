import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame containing the IDs of invalid tweets.

    A tweet is considered invalid if the number of characters in its 'content'
    field is strictly greater than 15.

    Args:
        tweets (pd.DataFrame): DataFrame with columns:
            - tweet_id (int): Unique identifier for the tweet.
            - content (str): The content of the tweet.

    Returns:
        pd.DataFrame: DataFrame with a single column 'tweet_id' containing
        the IDs of invalid tweets.

    Example:
        Input:
            tweet_id  content
        0         1   Hello!
        1         2   This tweet is way too long to be valid
        2         3   Normal

        Output:
            tweet_id
        0         2

    Time Complexity: O(N), where N is the number of rows in the DataFrame.
    Space Complexity: O(N), due to the filtered output.

    LeetCode: Beats 99.34% of submissions
    """
    return tweets[tweets["content"].str.len() > 15][["tweet_id"]]
