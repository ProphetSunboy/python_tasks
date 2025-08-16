class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        """
        Finds all peak indices in a 0-indexed mountain list.

        A peak is defined as an element that is strictly greater than its immediate neighbors.
        The first and last elements of the list cannot be peaks.

        Args:
            mountain (list[int]): The input list representing the mountain.

        Returns:
            list[int]: A list of indices where the peaks are located.

        Example:
            >>> findPeaks([1, 3, 2, 4, 1])
            [1, 3]

        Time Complexity: O(n)
        Space Complexity: O(1) (excluding the output list)

        LeetCode: Beats 100% of submissions
        """
        peaks = []

        for i in range(1, len(mountain) - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                peaks.append(i)

        return peaks
