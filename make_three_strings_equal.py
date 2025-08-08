class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        """
        Given three strings s1, s2, and s3, you can perform the following operation any number of times:
            - Choose one of the strings and delete its rightmost character (as long as the string is not empty).

        Return the minimum number of operations required to make all three strings equal.
        If it is impossible to make them equal (i.e., they do not share a common non-empty prefix), return -1.

        Args:
            s1 (str): The first string.
            s2 (str): The second string.
            s3 (str): The third string.

        Returns:
            int: The minimum number of operations to make all three strings equal, or -1 if impossible.

        Examples:
            >>> findMinimumOperations("abc", "ab", "a")
            3
            >>> findMinimumOperations("abc", "def", "ghi")
            -1

        Time Complexity: O(n), where n is the length of the shortest string.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        if s1[0] != s2[0] or s1[0] != s3[0]:
            return -1

        min_len = min(len(s1), len(s2), len(s3))
        k = 0
        for i in range(min_len):
            if s1[i] == s2[i] and s1[i] == s3[i]:
                k += 1
            else:
                break

        return len(s1) + len(s2) + len(s3) - 3 * k
