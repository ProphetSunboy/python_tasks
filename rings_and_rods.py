class Solution:
    def countPoints(self, rings: str) -> int:
        """Counts the number of rods that have rings of all three colors (red, green, and blue).

        The input string represents rings placed on rods numbered 0-9, where each ring is
        described by a color-position pair. Colors are 'R' (red), 'G' (green), or 'B' (blue),
        and positions are digits '0'-'9'.

        Args:
            rings (str): String of length 2n where each pair of characters represents
                        a ring's color and position (e.g., "R3G2B1")

        Returns:
            int: Number of rods that have all three colors of rings

        Examples:
            >>> countPoints("R3G2B1")
            0  # No rod has all three colors
            >>> countPoints("R0G0B0")
            1  # Rod 0 has all three colors

        Time complexity: O(n) - where n is length of rings string
        Space complexity: O(1) - constant space for rods list

        LeetCode: Beats 100% of submissions
        """
        rods = []
        colors = {"R": 0, "G": 1, "B": 2}

        for _ in range(10):
            rods.append([0, 0, 0])

        for i in range(0, len(rings), 2):
            rods[int(rings[i + 1])][colors[rings[i]]] = 1

        return sum([all(rod) for rod in rods])
