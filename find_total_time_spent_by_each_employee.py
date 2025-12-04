import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the total time spent by each employee in the office on each day.

    Table: Employees

    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | emp_id      | int  |
    | event_day   | date |
    | in_time     | int  |
    | out_time    | int  |
    +-------------+------+

    (emp_id, event_day, in_time) is the primary key for this table.
    Each row records one entry of an employee's arrival (in_time) and departure
    (out_time) on a given day (event_day).
    Employees may enter and leave the office multiple times in a single day.
    The total time spent in the office during one entry is out_time - in_time.

    Args:
        employees (pd.DataFrame): DataFrame with the columns:
            - emp_id (int): Employee ID.
            - event_day (date): Day of the event.
            - in_time (int): Arrival time (minute of day, 1-1440).
            - out_time (int): Departure time (minute of day, 1-1440).

    Returns:
        pd.DataFrame: DataFrame with columns ['day', 'emp_id', 'total_time'], where:
            - day: Day of the event (from event_day).
            - emp_id: Employee ID.
            - total_time: Total minutes spent at the office by that employee on
            that day.

    Example:
        Input:
            emp_id | event_day | in_time | out_time
            -------+-----------+---------+---------
            1      | 2023-07-14|   180   |   300
            1      | 2023-07-14|   400   |   600
            2      | 2023-07-14|   200   |   220

        Output:
            day        | emp_id | total_time
            -----------+--------+------------
            2023-07-14 |   1    |   320
            2023-07-14 |   2    |   20

    Time Complexity: O(N), where N is the number of events (rows in employees DataFrame).
    Space Complexity: O(N), for storing the resulting grouped and aggregated DataFrame.

    LeetCode: Beats 94.65% of submissions
    """
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    return (
        employees.groupby(["event_day", "emp_id"])["total_time"]
        .sum()
        .reset_index()
        .rename(columns={"event_day": "day"})
    )
