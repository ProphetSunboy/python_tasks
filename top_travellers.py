import pandas as pd


def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    """
    Reports the distance traveled by each user.

    Tables:
        Users
            - id (int): Unique user identifier.
            - name (varchar): Name of the user.

        Rides
            - id (int): Unique ride identifier.
            - user_id (int): ID of the user who traveled.
            - distance (int): Distance traveled in the ride.

    For each user, compute the total distance traveled.
    Return the result ordered by travelled_distance in descending order.
    If two or more users have the same travelled_distance,
    order them by name in ascending order.

    Returns:
        pd.DataFrame: DataFrame with each user's name and their corresponding
                      travelled_distance (sum of all rides).

    LeetCode: Beats 93.37% of submissions
    """
    distance_traveled = (
        rides[["user_id", "distance"]]
        .groupby("user_id")
        .sum()
        .reset_index()
        .rename(columns={"distance": "travelled_distance"})
    )
    users_traveled = users.merge(
        distance_traveled, how="left", left_on="id", right_on="user_id"
    ).drop(["id", "user_id"], axis=1)

    return users_traveled.fillna(0).sort_values(
        by=["travelled_distance", "name"], ascending=[False, True]
    )
