class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        """Counts the number of employees who met the working hours target.

        Args:
            hours (list[int]): A list of hours worked by each employee.
            target (int): The target number of hours.

        Returns:
            int: The number of employees who worked at least `target` hours.

        Example:
            >>> numberOfEmployeesWhoMetTarget(hours=[0, 1, 2, 3, 4], target=2)
            3
            >>> numberOfEmployeesWhoMetTarget(hours=[5, 1, 4, 2, 2], target=6)
            0

        LeetCode: Beats 100% of submissions
        """
        sorted_hours = sorted(hours)
        good_employees = 0

        for i in range(len(sorted_hours)):
            if sorted_hours[i] >= target:
                good_employees = len(sorted_hours) - i
                break

        return good_employees
