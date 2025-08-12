class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        """
        Given a list of logs where each log is [birth, death], representing the birth and death years of a person,
        this function finds the earliest year with the maximum population.

        A person is considered alive from their birth year up to (but not including) their death year.

        Args:
            logs (List[List[int]]): Each element is [birth, death] for a person.

        Returns:
            int: The earliest year with the maximum population.

        Example:
            >>> maximumPopulation([[1993,1999],[2000,2010]])
            1993

        Time Complexity: O(N + Y), where N is the number of logs and Y is the range of years considered.
        Space Complexity: O(Y), where Y is the range of years considered.

        LeetCode: Beats 100% of submissions
        """
        p = [0] * 100

        for log in logs:
            for i in range(log[0], log[1]):
                p[i - 1950] += 1

        max_p = max(p)
        for i, k in enumerate(p):
            if k == max_p:
                return i + 1950
