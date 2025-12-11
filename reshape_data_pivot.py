import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot the weather DataFrame so that each row corresponds to a unique month,
    and columns represent each city with its corresponding temperature values.

    Parameters:
        weather (pd.DataFrame): DataFrame with columns
            - city (object): Name of the city
            - month (object): Month
            - temperature (int): Temperature for that city and month

    Returns:
        pd.DataFrame: Pivoted DataFrame where rows are months, columns are city names,
                      and values are temperatures.

    Example:
        Input DataFrame (weather):

            city   month  temperature
        0  Beijing  Jan           5
        1  Beijing  Feb          10
        2  Shanghai Jan           7
        3  Shanghai Feb          15

        Output DataFrame:

        city   Beijing  Shanghai
        month
        Jan           5         7
        Feb          10        15

    Time Complexity: O(M), where M is the number of rows in the input DataFrame.
    Space Complexity: O(M).

    LeetCode: Beats 99.30% of submissions
    """
    return weather.pivot(index="month", columns="city", values="temperature")
