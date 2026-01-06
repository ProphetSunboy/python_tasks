import pandas as pd


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the Employees table to report managers and their direct reports.

    Table: Employees
        +-------------+----------+
        | Column Name | Type     |
        +-------------+----------+
        | employee_id | int      |
        | name        | varchar  |
        | reports_to  | int      |
        | age         | int      |
        +-------------+----------+
    employee_id is the unique key for this table.
    The table contains information about each employee, including the id of
    their manager (reports_to).
    Some employees do not report to anyone (reports_to is null).

    A manager is defined as an employee who has at least one other employee
    reporting to them.

    The function returns a DataFrame with the IDs and names of all managers,
    the number of employees who report directly to them, and the average age
    of those direct reports, rounded to the nearest integer. The result is
    ordered by employee_id.

    LeetCode: Beats 92.66% of submissions
    """
    grouped_df = employees.groupby("reports_to")

    managers = employees.merge(
        grouped_df.size().reset_index(), left_on="employee_id", right_on="reports_to"
    )
    managers = managers.merge(
        grouped_df["age"].mean().reset_index(),
        left_on="employee_id",
        right_on="reports_to",
    )

    managers.drop(
        ["reports_to_x", "age_x", "reports_to_y", "reports_to"], axis=1, inplace=True
    )
    managers.columns = ["employee_id", "name", "reports_count", "average_age"]
    managers["average_age"] = np.floor(managers["average_age"] + 0.5).astype(int)

    return managers.sort_values(by="employee_id")
