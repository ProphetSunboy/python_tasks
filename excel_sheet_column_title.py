class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        Given an integer columnNumber, return its corresponding column title as
        it appears in an Excel sheet.

        For example:

        A -> 1
        B -> 2
        C -> 3
        Z -> 26
        AA -> 27
        AB -> 28


        :param int columnNumber: number of excel column
        :returns str column_excel: corresponding column title
        the next greater element as described above

        Time complexity: O(log26n)
        Space complexity: O(log26n)

        LeetCode: Beats 99.09%
        """
        column_excel = ""

        while columnNumber > 0:
            column_excel = chr(65 + (columnNumber - 1) % 26) + column_excel
            columnNumber = (columnNumber - 1) // 26

        return column_excel
