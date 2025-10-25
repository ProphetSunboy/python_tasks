class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Convert an Excel-style column title (e.g., 'A', 'AB', 'ZY') to its corresponding column number.

        Args:
            columnTitle (str): The column title consisting of uppercase English letters.

        Returns:
            int: The corresponding column number.

        Example:
            >>> titleToNumber('A')
            1
            >>> titleToNumber('AB')
            28
            >>> titleToNumber('ZY')
            701

        Time Complexity: O(1), because columnTitle max value is "FXSHRXW".
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        cols = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26,
        }

        col_num = cols[columnTitle[-1]]
        curr = 1
        for i in range(len(columnTitle) - 2, -1, -1):
            col_num += cols[columnTitle[i]] * 26**curr
            curr += 1

        return col_num
