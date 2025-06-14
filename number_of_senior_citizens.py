# First solution
class Solution:
    def countSeniors(self, details: list[str]) -> int:
        """Counts the number of passengers who are strictly more than 60 years old.

        Given a list of passenger details where each string contains:
        - First 10 chars: Phone number
        - Next char: Gender
        - Next 2 chars: Age
        - Last 2 chars: Seat number

        Args:
            details (list[str]): List of passenger detail strings, each 15 chars long

        Returns:
            int: Number of passengers older than 60 years

        Examples:
            >>> countSeniors(["7868190130M7522", "5303914400F9211"])
            2  # Both passengers are over 60 (75 and 92 years old)
            >>> countSeniors(["1313579440F2036", "2921522980M5644"])
            0  # No passengers over 60 (20 and 56 years old)

        Time complexity: O(n) - where n is length of details list
        Space complexity: O(1) - only stores count

        LeetCode: Beats 100% of submissions
        """
        return len([1 for detail in details if detail[11:13] > "60"])
