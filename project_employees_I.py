import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    """
    Given two dataframes:

    - project: DataFrame with columns ['project_id', 'employee_id'] where each
    row indicates an employee assigned to a project.
    - employee: DataFrame with columns ['employee_id', 'name', 'experience_years']
    providing details about each employee.

    This function computes the average experience years of all employees for
    each project, rounding the result to two decimal places.

    Args:
        project (pd.DataFrame): DataFrame with project assignments.
        employee (pd.DataFrame): DataFrame with employee details.

    Returns:
        pd.DataFrame: DataFrame with columns ['project_id', 'average_years'],
        where 'average_years' is the average experience years for the project,
        rounded to two decimal places.

    Example:
        Input:
            project =
                project_id  employee_id
                1           101
                1           102
                2           101

            employee =
                employee_id  name    experience_years
                101          Alice   5
                102          Bob     3

        Output:
            project_id  average_years
            1           4.00
            2           5.00

    Time Complexity: O(n), where n is the number of project-employee assignments (merge + groupby).
    Space Complexity: O(n), due to intermediate merged and grouped DataFrames.

    LeetCode: Beats 93.54% of submissions
    """
    merged_df = project.merge(employee, how="left").drop(
        ["employee_id", "name"], axis=1
    )

    return (
        merged_df.groupby("project_id")
        .mean()
        .round(decimals=2)
        .reset_index()
        .rename(columns={"experience_years": "average_years"})
    )
