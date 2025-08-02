class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        """
        Counts the number of alternating groups in a circular list of red and blue tiles.

        An alternating group is defined as any three contiguous tiles in the circle
        where the middle tile has a different color from both its left and right neighbors.
        The circle is represented by the list `colors`, where:
            - colors[i] == 0: tile i is red
            - colors[i] == 1: tile i is blue

        Since the tiles form a circle, the first and last tiles are considered adjacent.

        Args:
            colors (list[int]): List representing the colors of the tiles (0 for red, 1 for blue).

        Returns:
            int: The number of alternating groups in the circle.

        Example:
            >>> numberOfAlternatingGroups([0, 1, 0, 1])
            4

        Time complexity: O(n), where n is the length of colors.
        Space complexity: O(1).

        LeetCode: Beats 97.83% of submissions
        """
        groups = 0

        for i in range(len(colors)):
            if (
                colors[i] != colors[i - 1]
                and colors[i] != colors[(i + 1) % len(colors)]
            ):
                groups += 1

        return groups
