class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """
        Given a row of n houses, each painted with a color represented by an integer in the list 'colors',
        returns the maximum distance between two houses with different colors.

        The distance between the ith and jth houses is defined as abs(i - j).

        Args:
            colors (List[int]): A list where colors[i] is the color of the ith house.

        Returns:
            int: The maximum distance between two houses with different colors.

        Example:
            >>> maxDistance([1,1,1,6,1,1,1])
            3

        Time Complexity: O(n), where n is the number of houses.
        Space Complexity: O(k), where k is the number of unique colors.

        LeetCode: Beats 100% of submissions
        """
        diff_colors = {}
        furthest = 0

        for i, color in enumerate(colors):
            if diff_colors.get(color, -1) == -1:
                diff_colors[color] = i

            for c, j in diff_colors.items():
                if color != c and i - j > furthest:
                    furthest = i - j

        return furthest
