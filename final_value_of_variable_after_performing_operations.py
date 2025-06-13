class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        """Calculates the final value of variable X after performing a series of increment/decrement operations.

        The operations can be one of four types:
        - ++X: Pre-increment X by 1
        - X++: Post-increment X by 1
        - --X: Pre-decrement X by 1
        - X--: Post-decrement X by 1

        Args:
            operations (list[str]): List of operation strings to perform

        Returns:
            int: Final value of X after all operations

        Examples:
            >>> finalValueAfterOperations(["--X","X++","X++"])
            1  # --X: -1, X++: +1, X++: +1, final = 1
            >>> finalValueAfterOperations(["++X","++X","X++"])
            3  # ++X: +1, ++X: +1, X++: +1, final = 3

        Time complexity: O(n) - where n is number of operations
        Space complexity: O(1) - constant space for counter

        LeetCode: Beats 100% of submissions
        """
        c = Counter(operations)
        x = 0

        for op, val in c.items():
            if "-" in op:
                x -= val
            else:
                x += val

        return x
