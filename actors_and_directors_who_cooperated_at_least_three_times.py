import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame representing the ActorDirector table with the following columns:
        - actor_id (int): ID of the actor
        - director_id (int): ID of the director
        - timestamp (int): Unique timestamp of a cooperation (primary key)

    This function returns all unique pairs of (actor_id, director_id) where the
    actor has collaborated with the director at least three times.

    Args:
        actor_director (pd.DataFrame): DataFrame with columns ['actor_id', 'director_id', 'timestamp']

    Returns:
        pd.DataFrame: DataFrame with columns ['actor_id', 'director_id'] for all qualifying pairs

    Example:
        Input:
            actor_director = pd.DataFrame({
                'actor_id': [1, 1, 1, 2, 2, 2, 2],
                'director_id': [10, 10, 10, 20, 20, 21, 21],
                'timestamp': [100, 101, 102, 103, 104, 105, 106]
            })
        Output:
            pd.DataFrame({
                'actor_id': [1],
                'director_id': [10]
            })
        Explanation:
            - (1, 10) cooperated 3 times → included
            - (2, 20) cooperated 2 times → not included
            - (2, 21) cooperated 2 times → not included

    Time Complexity: O(n), where n is the number of rows in the DataFrame
    Space Complexity: O(k), where k is the number of unique (actor_id, director_id) pairs

    LeetCode: Beats 98.92% of submissions
    """
    grouped_df = (
        actor_director.groupby(["actor_id", "director_id"]).count().reset_index()
    )
    return grouped_df[grouped_df["timestamp"] >= 3][["actor_id", "director_id"]]
