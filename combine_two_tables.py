import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """
    Combines the Person and Address tables to report information on each person
    along with their city and state if available.

    Args:
        person (pd.DataFrame): DataFrame containing personId (int), lastName (str), and firstName (str).
            - personId is the primary key for this table and uniquely identifies each person.
        address (pd.DataFrame): DataFrame containing addressId (int), personId (int), city (str), and state (str).
            - addressId is the primary key for this table. Each row links a personId with a city and state.

    Returns:
        pd.DataFrame: DataFrame with columns ["firstName", "lastName", "city", "state"] for each person in the Person table.
            - If a person's address is missing, "city" and "state" will be null for that row.

    Example:
        >>> person = pd.DataFrame({"personId": [1,2], "lastName":["Wang","Alice"], "firstName":["Allen","Bob"]})
        >>> address = pd.DataFrame({"addressId":[1],"personId":[2],"city":["New York"],"state":["NY"]})
        >>> combine_two_tables(person, address)
          firstName lastName      city state
        0     Allen     Wang      NaN   NaN
        1       Bob    Alice  New York    NY

    Time Complexity: O(P + A), where P is the number of rows in the Person table
    and A is the number of rows in the Address table (due to merging).
    Space Complexity: O(P + A), to hold the merged DataFrame.

    LeetCode: Beats 92.87% of submissions
    """
    return person.merge(address, on="personId", how="left")[
        ["firstName", "lastName", "city", "state"]
    ]
