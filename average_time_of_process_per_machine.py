import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the average process completion time for each machine.

    The input DataFrame `activity` has the following columns:
        - machine_id (int): The unique identifier for each machine.
        - process_id (int): The unique identifier for each process running on a machine.
        - activity_type (enum): Either 'start' or 'end', indicating whether the row marks the start or end of a process.
        - timestamp (float): The time when the activity occurred (in seconds).

    Each (machine_id, process_id) pair will have exactly two records:
        one with activity_type 'start' and one with 'end', with 'start' always before 'end'.

    The processing time for a process is (end timestamp) - (start timestamp).
    The average processing time per machine is the mean of all its process durations.

    Args:
        activity (pd.DataFrame): DataFrame with the following columns:
        - machine_id (int): The unique identifier for each machine.
        - process_id (int): The unique identifier for each process running on a machine.
        - activity_type (enum): Either 'start' or 'end', indicating whether the row marks the start or end of a process.
        - timestamp (float): The time when the activity occurred (in seconds).

    Returns:
        pd.DataFrame: DataFrame with columns:
            - machine_id (int)
            - processing_time (float): Average process time for the machine, rounded to 3 decimal places.

    Example:
        Input:
            activity = pd.DataFrame([
                [1, 101, 'start', 1.0],
                [1, 101, 'end',   4.0],
                [1, 102, 'start', 2.0],
                [1, 102, 'end',   5.0],
                [2, 201, 'start', 3.5],
                [2, 201, 'end',   8.5]
            ], columns=['machine_id', 'process_id', 'activity_type', 'timestamp'])

        Output:
            machine_id  processing_time
            1           3.0
            2           5.0

    Time Complexity: O(n), where n is the number of rows in activity.
    Space Complexity: O(n), due to intermediate merged DataFrame.

    LeetCode: Beats 91.81% of submissions
    """
    starts = activity[activity["activity_type"] == "start"]
    ends = activity[activity["activity_type"] == "end"]

    merged = pd.merge(
        starts, ends, on=["machine_id", "process_id"], suffixes=("_start", "_end")
    )

    merged["duration"] = merged["timestamp_end"] - merged["timestamp_start"]

    result = merged.groupby("machine_id")["duration"].mean().reset_index()

    result.columns = ["machine_id", "processing_time"]
    result["processing_time"] = result["processing_time"].round(3)

    return result
