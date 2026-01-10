import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the rows for patients who have Type I Diabetes.

    Args:
        patients : pd.DataFrame
            DataFrame containing patient data with columns:
            - patient_id (int): Unique identifier for the patient.
            - patient_name (str): Name of the patient.
            - conditions (str): Zero or more condition codes as a space-separated
            string. Type I Diabetes codes always start with 'DIAB1'.

    Returns:
        pd.DataFrame: DataFrame containing patient_id, patient_name, and
        conditions for patients who have at least one condition code starting
        with 'DIAB1'.

    Example
        Input:
            patient_id | patient_name | conditions
            -----------+--------------+--------------
            1         | Alice        | "A10 DIAB1X"
            2         | Bob          | "DIAB2"

        Output:
            patient_id | patient_name | conditions
            -----------+--------------+--------------
            1         | Alice        | "A10 DIAB1X"

    Time Complexity: O(n), where n is the number of patients.
    Space Complexity: O(1), not including the output DataFrame.

    LeetCode: Beats 97.02% of submissions
    """
    return patients[patients["conditions"].str.contains(r"(?:^|\s)DIAB1")]
