import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the ids of days where the temperature was higher than the previous
    day's temperature.

    Table Schema:
        Weather(
            id: int,            # unique identifier for each record
            recordDate: date,   # the date of the record (no duplicates)
            temperature: int    # the temperature for that date
        )

    For each day, compares the temperature to the previous day's (yesterday's)
    temperature (i.e., where (recordDate - 1 day) exists) and finds all ids
    where today's temperature is higher.

    Args:
        weather (pd.DataFrame): DataFrame with columns ['id', 'recordDate', 'temperature'].

    Returns:
        pd.DataFrame: DataFrame containing only the ['id'] of days with a
        rising temperature compared to the previous day.

    Example:

        Input:
        Weather table:
        +----+------------+-------------+
        | id | recordDate | temperature |
        +----+------------+-------------+
        | 1  | 2015-01-01 | 10          |
        | 2  | 2015-01-02 | 25          |
        | 3  | 2015-01-03 | 20          |
        | 4  | 2015-01-04 | 30          |
        +----+------------+-------------+
        Output:
        +----+
        | id |
        +----+
        | 2  |
        | 4  |
        +----+

    Time Complexity: O(n), where n is the number of rows in weather.
    Space Complexity: O(n), for intermediate Series.

    LeetCode: Beats 92.57% of submissions.
    """
    weather = weather.sort_values("recordDate")

    prev_date = weather["recordDate"].shift(1)
    prev_temp = weather["temperature"].shift(1)

    is_rising = (weather["recordDate"] - prev_date == pd.Timedelta(days=1)) & (
        weather["temperature"] > prev_temp
    )

    return weather[is_rising][["id"]]
