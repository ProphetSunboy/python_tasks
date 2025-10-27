class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Computes the total number of laser beams present in the bank.

        The bank is represented as a list of binary strings, where each string corresponds to a row of cells:
        - '1' indicates a cell with a security device.
        - '0' indicates an empty cell.

        A laser beam exists between every device in one row and every device in
        the next non-empty row (i.e., a row that contains at least one device),
        with all rows in between being empty.

        Args:
            bank (List[str]): List of strings representing the floor plan of the bank.

        Returns:
            int: The total number of laser beams in the bank.

        Example:
            >>> numberOfBeams(["011001","000000","010100","001000"])
            8
            >>> numberOfBeams(["000","111","000"])
            0

        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        total_beams = 0
        prev = 0
        for row in bank:
            devices = row.count("1")

            if devices > 0:
                total_beams += devices * prev
                prev = devices

        return total_beams
