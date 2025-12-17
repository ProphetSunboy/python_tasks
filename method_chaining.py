import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame containing the names of animals whose weight is strictly
    greater than 100 kilograms, sorted by weight in descending order.

    Args:
        animals (pd.DataFrame): A DataFrame with the following columns:
            - name (object): Animal's name
            - species (object): Animal's species
            - age (int): Animal's age
            - weight (int): Animal's weight in kilograms

    Returns:
        pd.DataFrame: A DataFrame with a single column 'name' listing the
        qualifying animals, sorted by weight descending.

    Example:
        Input:
            +-------+---------+-----+--------+
            | name  | species | age | weight |
            +-------+---------+-----+--------+
            | Leo   | Lion    | 5   | 190    |
            | Ellie | Elephant| 10  | 5400   |
            | Bob   | Bear    | 7   | 95     |
            +-------+---------+-----+--------+

        Output:
            +-------+
            | name  |
            +-------+
            | Ellie |
            | Leo   |
            +-------+

    Time: O(N log N) due to the sorting step
    Space: O(1) (excluding output, as DataFrame views are used)

    LeetCode: Beats 98.48% of submissions
    """
    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[
        ["name"]
    ]
