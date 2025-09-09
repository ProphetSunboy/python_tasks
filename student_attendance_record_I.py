class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        Determines if a student is eligible for an attendance award based on their attendance record.

        The attendance record is a string consisting of the following characters:
            'A': Absent
            'L': Late
            'P': Present

        Eligibility criteria:
            - The student has fewer than 2 absences ('A').
            - The student is never late ('L') for 3 or more consecutive days.

        Args:
            s (str): The attendance record string.

        Returns:
            bool: True if the student is eligible for the award, False otherwise.

        Example:
            >>> checkRecord("PPALLP")
            True
            >>> checkRecord("PPALLL")
            False

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        absent = 0
        cons_late = 0

        for ch in s:
            if ch == "A":
                absent += 1
                cons_late = 0
                if absent == 2:
                    return False
            elif ch == "L":
                cons_late += 1
                if cons_late == 3:
                    return False
            else:
                cons_late = 0

        return True
