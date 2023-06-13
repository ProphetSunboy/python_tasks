# First approach
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Given a 0-indexed n x n integer matrix grid, return the number of pairs
        (ri, cj) such that row ri and column cj are equal.

        A row and column pair is considered equal if they contain the same
        elements in the same order (i.e., an equal array).
        """
        counter = 0
        cols = {}

        for i in range(len(grid)):
            col = [grid[j][i] for j in range(len(grid))]

            col = tuple(col)
            
            if col not in cols:
                cols[col] = 1
            else:
                cols[col] += 1

        for row in grid:
            counter += cols.get(tuple(row), 0)

        return counter
    

# Second approach
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        
        # Keep track of the frequency of each row.
        row_counter = collections.Counter(tuple(row) for row in grid)

        # Add up the frequency of each column in map.
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

            
        return count