import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the daily count of active users for each of the 30 days ending on
    2019-07-27 (inclusive).

    A user is considered active on a given day if they performed at least one
    activity (of any type) on that day.

    Table Schema:
        Activity(
            user_id: int,        # unique user identifier
            session_id: int,     # unique session identifier (each session belongs to exactly one user)
            activity_date: date, # date of user activity
            activity_type: enum  # type of activity: one of ('open_session', 'end_session', 'scroll_down', 'send_message')
        )
        Note: Table may contain duplicate rows.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - day (date): the activity date
            - active_users (int): number of unique users active on that day

    Example:
        Input:
        Activity table:
        +---------+------------+---------------+---------------+
        | user_id | session_id | activity_date | activity_type |
        +---------+------------+---------------+---------------+
        | 1       | 1          | 2019-07-20    | open_session  |
        | 1       | 1          | 2019-07-20    | scroll_down   |
        | 1       | 1          | 2019-07-20    | end_session   |
        | 2       | 4          | 2019-07-20    | open_session  |
        | 2       | 4          | 2019-07-21    | send_message  |
        | 2       | 4          | 2019-07-21    | end_session   |
        | 3       | 2          | 2019-07-21    | open_session  |
        | 3       | 2          | 2019-07-21    | send_message  |
        | 3       | 2          | 2019-07-21    | end_session   |
        | 4       | 3          | 2019-06-25    | open_session  |
        | 4       | 3          | 2019-06-25    | end_session   |
        +---------+------------+---------------+---------------+
        Output:
        +------------+--------------+
        | day        | active_users |
        +------------+--------------+
        | 2019-07-20 | 2            |
        | 2019-07-21 | 2            |
        +------------+--------------+
    Time Complexity: O(n), where n is the number of activity records in the input DataFrame.
    Space Complexity: O(k), where k is the number of unique days in the 30-day period.

    LeetCode: Beats 97.04% of submissions.
    """
    activity = activity[activity["activity_date"].between("2019-06-28", "2019-07-27")]

    return (
        activity.groupby("activity_date", as_index=False)["user_id"]
        .nunique()
        .rename(columns={"activity_date": "day", "user_id": "active_users"})
    )
