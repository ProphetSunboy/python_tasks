class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        Simulates folder navigation operations in a file system and returns the
        minimum number of operations needed to return to the main folder.

        The file system supports the following operations:
            - "../": Move to the parent folder (if already at the main folder, stay there).
            - "./": Remain in the current folder.
            - "x/": Move to the child folder named x (guaranteed to exist).

        Args:
            logs (List[str]): A list of folder navigation operations.

        Returns:
            int: The minimum number of operations required to return to the main folder after performing all operations.

        Example:
            >>> minOperations(["d1/", "d2/", "../", "d21/", "./"])
            2
            >>> minOperations(["d1/", "../", "../", "../"])
            0

        Time Complexity: O(n), where n is the number of operations in logs.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        depth = 0

        for log in logs:
            if log == "../":
                if depth:
                    depth -= 1
            elif log == "./":
                continue
            else:
                depth += 1

        return depth
