import pandas as pd


def sales_person(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
    """
    Given the tables:

    SalesPerson
    +-----------------+---------+
    | sales_id        | int     |  # Primary Key
    | name            | varchar |
    | salary          | int     |
    | commission_rate | int     |
    | hire_date       | date    |
    +-----------------+---------+

    Company
    +-------------+---------+
    | com_id      | int     |  # Primary Key
    | name        | varchar |
    | city        | varchar |
    +-------------+---------+

    Orders
    +-------------+------+
    | order_id    | int  |  # Primary Key
    | order_date  | date |
    | com_id      | int  |  # Foreign Key to Company.com_id
    | sales_id    | int  |  # Foreign Key to SalesPerson.sales_id
    | amount      | int  |
    +-------------+------+

    Return the names of all salespersons who did not have any orders
    involving the company named "RED".

    Args:
        sales_person (pd.DataFrame): Data for SalesPerson table.
        company (pd.DataFrame): Data for Company table.
        orders (pd.DataFrame): Data for Orders table.

    Returns:
        pd.DataFrame: A DataFrame containing the "name" column for all salespersons
                      with no orders related to "RED".

    Example:
        Input:
        SalesPerson table:
        +----------+------+--------+-----------------+------------+
        | sales_id | name | salary | commission_rate | hire_date  |
        +----------+------+--------+-----------------+------------+
        | 1        | John | 100000 | 6               | 4/1/2006   |
        | 2        | Amy  | 12000  | 5               | 5/1/2010   |
        | 3        | Mark | 65000  | 12              | 12/25/2008 |
        | 4        | Pam  | 25000  | 25              | 1/1/2005   |
        | 5        | Alex | 5000   | 10              | 2/3/2007   |
        +----------+------+--------+-----------------+------------+
        Company table:
        +--------+--------+----------+
        | com_id | name   | city     |
        +--------+--------+----------+
        | 1      | RED    | Boston   |
        | 2      | ORANGE | New York |
        | 3      | YELLOW | Boston   |
        | 4      | GREEN  | Austin   |
        +--------+--------+----------+
        Orders table:
        +----------+------------+--------+----------+--------+
        | order_id | order_date | com_id | sales_id | amount |
        +----------+------------+--------+----------+--------+
        | 1        | 1/1/2014   | 3      | 4        | 10000  |
        | 2        | 2/1/2014   | 4      | 5        | 5000   |
        | 3        | 3/1/2014   | 1      | 1        | 50000  |
        | 4        | 4/1/2014   | 1      | 4        | 25000  |
        +----------+------------+--------+----------+--------+
        Output:
        +------+
        | name |
        +------+
        | Amy  |
        | Mark |
        | Alex |
        +------+

    Time Complexity: O(n), where n is the number of orders (for filtering).
    Space Complexity: O(m), where m is the number of salespersons (for output).

    LeetCode: Beats 91.70% of submissions
    """
    red_id = company[company["name"] == "RED"]["com_id"]

    related_ids = orders[orders["com_id"].isin(red_id)]["sales_id"].unique()

    return sales_person[~sales_person["sales_id"].isin(related_ids)][["name"]]
