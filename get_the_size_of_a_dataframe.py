import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    """
    Returns the size of the 'players' DataFrame as [number of rows, number of columns].

    Args:
        players (pd.DataFrame): A pandas DataFrame containing player data.

    Returns:
        List[int]: A list containing two integers:
            - The number of rows in the DataFrame
            - The number of columns in the DataFrame

    Example:
        If players has 3 rows and 4 columns, the function returns [3, 4].

    Time Complexity: O(1)
    Space Complexity: O(1)

    LeetCode: Beats 96.53% of submissions
    """
    return [len(players), len(players.columns)]
