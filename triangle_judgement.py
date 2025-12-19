import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame 'triangle' with columns:
      - x (int)
      - y (int)
      - z (int)
    Each row represents the lengths of three line segments.

    Determines for each row whether the segments (x, y, z) can form a valid triangle
    (i.e., the sum of the lengths of any two sides is greater than the third side).

    Args:
        triangle (pd.DataFrame): A DataFrame with columns 'x', 'y', 'z', each
        representing the lengths of triangle sides for each row.

    Returns:
        pd.DataFrame: The input DataFrame with an additional column 'triangle' that
        contains "Yes" if (x, y, z) can form a triangle, otherwise "No".

    Example:
        Input DataFrame:
            x  y  z
         0  2  4  7
         1  3  4  5

        Output DataFrame:
            x  y  z triangle
         0  2  4  7      No
         1  3  4  5     Yes

    Time Complexity: O(N) where N is the number of rows in the DataFrame, since each row is checked once.
    Space Complexity: O(1) (excluding the output column).

    LeetCode: Beats 97.82% of submissions
    """
    triangle["triangle"] = (
        (triangle["x"] + triangle["y"] > triangle["z"])
        & (triangle["x"] + triangle["z"] > triangle["y"])
        & (triangle["y"] + triangle["z"] > triangle["x"])
    )
    triangle["triangle"] = (
        triangle["triangle"].astype(object).replace({False: "No", True: "Yes"})
    )
    return triangle
