class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Compare two version strings, version1 and version2.

        Each version string consists of revisions separated by dots ('.').
        Each revision is an integer (leading zeros are ignored).
        Compare the revisions in left-to-right order.
        If one version string has fewer revisions, treat the missing revisions as 0.

        Returns:
            int:
                -1 if version1 < version2,
                 1 if version1 > version2,
                 0 if they are equal.

        Example:
            >>> compareVersion("1.01", "1.001")
            0
            >>> compareVersion("1.0", "1.0.0")
            0
            >>> compareVersion("0.1", "1.1")
            -1

        Time Complexity: O(max(N, M)), where N and M are the number of revisions in version1 and version2.
        Space Complexity: O(N + M)

        LeetCode: Beats 100% of submissions
        """
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        if len(v1) < len(v2):
            v1 += [0] * (len(v2) - len(v1))
        elif len(v1) > len(v2):
            v2 += [0] * (len(v1) - len(v2))

        for v1_rev, v2_rev in zip(v1, v2):
            if v1_rev < v2_rev:
                return -1
            elif v1_rev > v2_rev:
                return 1

        return 0
