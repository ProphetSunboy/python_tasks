import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    """
    Given a pandas DataFrame `my_numbers` with a single column "num", where each
    row contains an integer and duplicates are allowed, find the largest integer
    that appears exactly once ("single number").
    If there are no such numbers, return a DataFrame with {"num": None}.

    Args:
        my_numbers (pd.DataFrame): DataFrame with a single column "num"
                                containing integers.

    Returns:
        pd.DataFrame: DataFrame containing the largest single number in the "num" column.
                      If no single number exists, returns DataFrame with {"num": None}.

    Example:
        Input:
            my_numbers = pd.DataFrame({"num": [8, 2, 8, 3]})
        Output:
            pd.DataFrame({"num": [3]})
        (since 3 and 2 appear once, 3 is larger)

    Time Complexity: O(n), as we rely on set and pandas operations over all n rows.
    Space Complexity: O(n), for storing intermediate DataFrames.

    LeetCode: Beats 98.15% of submissions
    """
    empty = pd.DataFrame({"num": None}, index=[0])
    single_nums = my_numbers.drop_duplicates(keep=False)
    res = single_nums[single_nums["num"] == single_nums["num"].max()]

    return res if len(res) == 1 else empty
