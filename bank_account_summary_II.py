import pandas as pd


def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the name and balance for users whose account balance exceeds 10,000.

    Tables:
        Users:
            - account (int): Primary key. Account number for the user.
            - name (varchar): Name of the user (unique).

        Transactions:
            - trans_id (int): Primary key. Transaction identifier.
            - account (int): Account number involved in the transaction.
            - amount (int): Transaction amount. Positive for incoming funds,
            negative for outgoing.
            - transacted_on (date): Date of transaction.

    The balance for each account is defined as the sum of all amounts for that account,
    and all accounts start with an initial balance of 0.

    Args:
        users (pd.DataFrame): DataFrame containing user account and name information.
        transactions (pd.DataFrame): DataFrame of transactions made on the accounts.

    Returns:
        pd.DataFrame: DataFrame with two columns:
            - name (str): Name of the user.
            - balance (int): Total balance for the user.
        Only users with a balance greater than 10,000 are included.

    Example:
        Input:
            users:
                account | name
                ------- | ----
                1       | Alice
                2       | Bob

            transactions:
                trans_id | account | amount | transacted_on
                -------- | ------- | ------ | -------------
                10       | 1       | 12000  | 2024-01-02
                11       | 2       | 9000   | 2024-01-02

        Output:
            name   | balance
            ------ | -------
            Alice  | 12000

    Time Complexity: O(M + U), where M is the number of transactions and U is the number of users.
    Space Complexity: O(U), for storing balances.

    LeetCode: Beats 95.05% of submissions
    """
    balances = (
        transactions.groupby("account")["amount"].sum().reset_index(name="balance")
    )

    result = users.merge(balances, on="account", how="left")

    return result[result["balance"] > 10000][["name", "balance"]]
