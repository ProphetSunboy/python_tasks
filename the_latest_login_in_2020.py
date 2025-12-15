import pandas as pd


def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the latest login timestamp for each user, considering only logins
    from the year 2020.
    Only users that logged in during 2020 will be included. For each user, only
    their most recent 2020 login is reported.

    Args:
        logins (pd.DataFrame): DataFrame containing login records with columns:
            - user_id (int): Identifier for each user.
            - time_stamp (datetime): Timestamp of the login event.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - user_id: int
            - last_stamp: datetime (the most recent login time in 2020 for each user)

    Example:
        Input:
            logins =
                user_id  time_stamp
                1        2020-01-02 10:00:00
                2        2021-05-11 14:40:21
                1        2020-10-12 13:45:00
                3        2020-05-15 09:00:00
                2        2020-03-05 15:30:00

        Output:
            user_id  last_stamp
            1        2020-10-12 13:45:00
            2        2020-03-05 15:30:00
            3        2020-05-15 09:00:00

    Time Complexity: O(N log N), where N is the number of rows in the DataFrame (due to sorting).
    Space Complexity: O(N), for filtered and intermediate DataFrames.

    LeetCode: Beats 97.44% of submissions
    """
    return (
        logins[logins["time_stamp"].dt.year == 2020]
        .sort_values(by="time_stamp", ascending=False)
        .drop_duplicates(subset=["user_id"])
        .rename(columns={"time_stamp": "last_stamp"})
    )
