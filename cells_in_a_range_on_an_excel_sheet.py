class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        """
        Given a string s representing a range of cells in an Excel sheet in the format "<col1><row1>:<col2><row2>",
        where <col1> and <col2> are column letters ('A'-'Z') and <row1> and <row2> are row numbers (1-9),
        return a list of all cell names in the range, sorted first by column then by row.

        Each cell is represented as a string "<col><row>".

        Args:
            s (str): The range string, e.g., "A1:C2".

        Returns:
            List[str]: List of cell names in the specified range, sorted by column then row.

        Example:
            >>> cellsInRange("A1:B2")
            ['A1', 'A2', 'B1', 'B2']

        Time Complexity: O((number of columns) * (number of rows))
        Space Complexity: O((number of columns) * (number of rows))

        LeetCode: Beats 100% of submissions
        """
        start_row = int(s[1])
        end_row = int(s[4])

        start_col = ord(s[0])
        end_col = ord(s[3]) + 1

        cells = []
        for col in range(start_col, end_col):
            curr_col = chr(col)
            for row in range(start_row, end_row + 1):
                cells.append(curr_col + str(row))

        return cells
