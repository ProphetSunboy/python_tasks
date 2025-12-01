class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        Calculates the maximum number of minutes all n computers can run
        simultaneously using the provided batteries.

        Problem Description:
            - You have n computers and a list batteries where batteries[i] is
            the capacity (in minutes) of the ith battery.
            - Each computer can have at most one battery inserted at any time.
            - At any moment, you may freely swap batteries between computers or
            replace them with unused ones.
            - Batteries cannot be recharged.

        The goal is to maximize the total running time (in minutes) during which
        all n computers are running at the same time.

        Args:
            n (int): The number of computers.
            batteries (List[int]): The collection of available batteries, with
            each element representing its capacity in minutes.

        Returns:
            int: The maximum number of minutes all computers can run simultaneously.

        Example:
            Input:
                n = 2
                batteries = [3, 3, 3]
            Output:
                4

        Time Complexity: O(m log m), where m is the length of batteries (due to sorting).
        Space Complexity: O(m), for storing the sorted batteries.

        LeetCode: Beats 95.71% of submissions
        """
        batteries.sort()
        extra = sum(batteries[:-n])

        live = batteries[-n:]

        for i in range(n - 1):
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra // (i + 1)

            extra -= (i + 1) * (live[i + 1] - live[i])

        return live[-1] + extra // n
