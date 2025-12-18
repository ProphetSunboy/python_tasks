import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame `cinema` with the following columns:
        - id (int): Unique identifier for each movie.
        - movie (string): Name of the movie.
        - description (string): A description of the movie.
        - rating (float): The movie's rating, two decimal places, in the range [0, 10].

    Returns a DataFrame of movies that satisfy BOTH:
        1. The movie's `id` is odd.
        2. The `description` is not "boring".

    The output is sorted by `rating` in descending order.

    Args:
        cinema (pd.DataFrame): The input DataFrame with movie information.

    Returns:
        pd.DataFrame: Filtered and sorted DataFrame as described above.

    Example:
        Input:
            cinema =
                id  movie     description   rating
                1   MovieA    not boring    8.7
                2   MovieB    boring        9.0
                3   MovieC    exciting      9.5
        Output:
                id  movie     description   rating
                3   MovieC    exciting      9.5
                1   MovieA    not boring    8.7

    Time Complexity: O(N log N) for sorting.
    Space Complexity: O(N) for filtering and sorting.

    LeetCode: Beats 98.03% of submissions
    """
    return cinema[(cinema["id"] % 2) & (cinema["description"] != "boring")].sort_values(
        by="rating", ascending=False
    )
