import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    Reshapes the sales data so that each row represents the sales for a product in a specific quarter.

    The input DataFrame 'report' has the following schema:
        +----------+-----------+
        | product  | object    |
        | quarter_1| int       |
        | quarter_2| int       |
        | quarter_3| int       |
        | quarter_4| int       |
        +----------+-----------+

    Args:
        report (pd.DataFrame): DataFrame where each row is a product and each column after 'product'
                               is sales data for a quarter.

    Returns:
        pd.DataFrame: DataFrame with columns ['product', 'quarter', 'sales'], where each row represents
                      the sales of a product in a specific quarter.

    Example:
        Input:
            product | quarter_1 | quarter_2 | quarter_3 | quarter_4
            --------+-----------+-----------+-----------+-----------
               A    |   100     |   150     |   200     |   130
               B    |   90      |   110     |   120     |   140

        Output:
            product |  quarter  | sales
            --------+-----------+------
               A    | quarter_1 | 100
               A    | quarter_2 | 150
               A    | quarter_3 | 200
               A    | quarter_4 | 130
               B    | quarter_1 | 90
               B    | quarter_2 | 110
               B    | quarter_3 | 120
               B    | quarter_4 | 140

    Time Complexity: O(N*M), where N is the number of products and M is the number of quarters.
    Space Complexity: O(N*M), due to the reshaped DataFrame.

    LeetCode: Beats 97.15% of submissions
    """
    return report.melt(id_vars="product", var_name="quarter", value_name="sales")
