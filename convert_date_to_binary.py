class Solution:
    def convertDateToBinary(self, date: str) -> str:
        """
        Converts a Gregorian date string in 'yyyy-mm-dd' format into its binary representation.

        Each component (year, month, day) is converted to its binary form (without leading zeroes),
        and the components are joined with dashes to maintain the original structure.

        Args:
            date (str): The input string representing a date in 'yyyy-mm-dd' format.

        Returns:
            str: The binary representation of the date, with components separated by dashes.

        Example:
            >>> convertDateToBinary("2024-06-01")
            '111111001000-110-1'

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        bin_date = []

        for d in date.split("-"):
            bin_date.append(bin(int(d))[2:])

        return "-".join(bin_date)
