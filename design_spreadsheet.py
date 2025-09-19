class Spreadsheet:
    """
    Spreadsheet class implements a simple spreadsheet with 26 columns (labeled 'A' to 'Z') and a configurable number of rows.
    Each cell holds an integer value between 0 and 10^5 (inclusive).

    Methods:
        __init__(rows: int)
            Initializes the spreadsheet with the specified number of rows. All cells are set to 0.

        setCell(cell: str, value: int) -> None
            Sets the value of the specified cell.
            - cell: String in the format "AX" (e.g., "A1", "B10"), where the letter is the column ('A'-'Z') and the number is the 1-indexed row.
            - value: Integer to set in the cell.

        resetCell(cell: str) -> None
            Resets the specified cell to 0.
            - cell: String in the format "AX".

        getValue(formula: str) -> int
            Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers.
            Returns the computed sum.
            - If a referenced cell has not been set, its value is considered 0.

    Example:
        >>> ss = Spreadsheet(3)
        >>> ss.setCell("A1", 5)
        >>> ss.setCell("B2", 10)
        >>> ss.getValue("=A1+B2")
        15
        >>> ss.getValue("=A1+7")
        12
        >>> ss.resetCell("A1")
        >>> ss.getValue("=A1+B2")
        10
    """

    def __init__(self, rows: int):
        self.spreadsheet = {chr(i): [0] * rows for i in range(65, 91)}

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        i = int(cell[1:]) - 1
        self.spreadsheet[col][i] = value

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        i = int(cell[1:]) - 1
        self.spreadsheet[col][i] = 0

    def getValue(self, formula: str) -> int:
        vals = formula.replace("=", "").split("+")
        res = 0

        if vals[0][0].isalpha():
            col = vals[0][0]
            i = int(vals[0][1:]) - 1
            res += self.spreadsheet[col][i]
        else:
            res += int(vals[0])

        if vals[1][0].isalpha():
            col = vals[1][0]
            i = int(vals[1][1:]) - 1
            res += self.spreadsheet[col][i]
        else:
            res += int(vals[1])

        return res
