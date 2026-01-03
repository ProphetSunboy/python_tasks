import pandas as pd


def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze AI prompt usage patterns per user.

    Table: prompts

        +-------------+---------+
        | Column Name | Type    |
        +-------------+---------+
        | user_id     | int     |
        | prompt      | varchar |
        | tokens      | int     |
        +-------------+---------+
        (user_id, prompt) is the primary key for this table.
        Each row represents a prompt submitted by a user to an AI system,
        along with the number of tokens consumed.

    For each user:
        - Calculate the total number of prompts submitted.
        - Calculate the average tokens used per prompt (rounded to 2 decimal places).
        - Only include users who have submitted at least 3 prompts.
        - Only include users who have submitted at least one prompt with
          tokens greater than their own average token usage.
        - Return the result table ordered by average tokens (descending),
          then by user_id (ascending).

    LeetCode: Beats 100% of submissions
    """
    user_prompts = prompts.groupby("user_id")

    prompt_count = user_prompts.size()
    prompt_count = (
        prompt_count[prompt_count >= 3]
        .reset_index()
        .rename(columns={0: "prompt_count"})
    )
    avg_tokens = (
        user_prompts["tokens"]
        .mean()
        .round(decimals=2)
        .reset_index()
        .rename(columns={"tokens": "avg_tokens"})
    )
    unique_tokens = user_prompts.nunique()["tokens"]
    unique_tokens = unique_tokens[unique_tokens > 1].reset_index()

    valid_tokens = avg_tokens[avg_tokens["user_id"].isin(unique_tokens["user_id"])]
    res = prompt_count.merge(valid_tokens)

    return res.sort_values(by=["avg_tokens", "user_id"], ascending=[False, True])
