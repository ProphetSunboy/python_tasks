class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        """
        Counts the number of "covered" buildings in an n x n city grid.

        A building is represented by its coordinates [x, y] in the `buildings` list.
        A building is considered "covered" if there is at least one building
        directly to its left, right, above, and below (i.e., sharing the same row or column).

        Args:
            n (int): Size of the city (n x n grid).
            buildings (List[List[int]]): List of [x, y] coordinates for each building.

        Returns:
            int: The number of covered buildings.

        Example:
            Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
            Output: 1
            Explanation: Only the building at [2,2] has buildings on all four sides.

        Time Complexity: O(M log M), where M is the number of buildings,
            due to sorting step per row and column.
        Space Complexity: O(M).
        """
        rows = {}
        cols = {}

        for x, y in buildings:
            rows.setdefault(x, []).append(y)
            cols.setdefault(y, []).append(x)

        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()

        covered = 0

        for x, y in buildings:
            row = rows[x]
            col = cols[y]

            i = bisect_left(row, y)
            j = bisect_left(col, x)

            has_left = i > 0
            has_right = i + 1 < len(row)
            has_up = j > 0
            has_down = j + 1 < len(col)

            if has_left and has_right and has_up and has_down:
                covered += 1

        return covered
