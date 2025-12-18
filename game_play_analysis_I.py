import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame `activity`, each row represents a player's login/session
    on a specific day and device.
    Find the first login date (earliest `event_date`) for each `player_id`.

    Args:
        activity (pd.DataFrame): DataFrame containing game session information with columns:
            - player_id (int): Unique identifier for each player.
            - device_id (int): Device used during session.
            - event_date (date): Date of activity.
            - games_played (int): Number of games played in that session.

    Returns:
        pd.DataFrame: DataFrame with columns
            - player_id
            - first_login (earliest event_date per player)
        Result can be in any order.

    Example:
        Input:
            activity =
                player_id  device_id  event_date   games_played
                1          2          2023-06-01   5
                1          1          2023-05-30   2
                2          1          2023-07-01   8
        Output:
            player_id  first_login
            1          2023-05-30
            2          2023-07-01

    Time Complexity: O(N log N) due to sorting.
    Space Complexity: O(N).

    LeetCode: Beats 95.11% of submissions
    """
    return (
        activity.sort_values(by=["event_date"])
        .drop_duplicates(subset=["player_id"])[["player_id", "event_date"]]
        .rename(columns={"event_date": "first_login"})
    )
