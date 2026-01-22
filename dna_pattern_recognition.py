import pandas as pd


def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze DNA patterns in the Samples dataframe.

    The Samples table contains the following columns:
        - sample_id (int): Unique key for the sample.
        - dna_sequence (varchar): DNA sequence string containing characters A, T, G, C.
        - species (varchar): Species from which the sample was collected.

    Biologists are interested in identifying sample_ids with the following DNA sequence patterns:
        - Sequences that start with 'ATG' (a common start codon).
        - Sequences that end with either 'TAA', 'TAG', or 'TGA' (stop codons).
        - Sequences containing the motif 'ATAT' (a simple repeated pattern).
        - Sequences with at least 3 consecutive 'G' characters ('GGG', 'GGGG', etc.).

    Args:
        samples (pd.DataFrame): DataFrame with columns 'sample_id', 'dna_sequence', 'species'.

    Returns:
        pd.DataFrame: The input DataFrame with four additional columns indicating the
            presence (1) or absence (0) of each DNA pattern.

    Time Complexity: O(n), where n is the number of rows in the DataFrame.
    Space Complexity: O(n)

    LeetCode: Beats 90.60% of submissions
    """
    samples["has_start"] = samples["dna_sequence"].str.startswith("ATG").astype(int)

    samples["has_stop"] = (
        samples["dna_sequence"].str.contains(r"(TAA|TAG|TGA)$", regex=True).astype(int)
    )

    samples["has_atat"] = (
        samples["dna_sequence"].str.contains("ATAT", regex=False).astype(int)
    )
    samples["has_ggg"] = (
        samples["dna_sequence"].str.contains("GGG", regex=False).astype(int)
    )

    return samples
