class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """
        Return the number of possible unique paths that the robot can take to
        reach the bottom-right corner.

        You are given an m x n integer array grid. There is a robot initially
        located at the top-left corner (i.e., grid[0][0]). The robot tries to
        move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot
        can only move either down or right at any point in time.

        An obstacle and space are marked as 1 or 0 respectively in grid. A path
        that the robot takes cannot include any square that is an obstacle.

        :param list[list[int]] obstacleGrid: grid of obstacles and spaces
        :returns int unique_paths: the number of possible unique paths that the robot can take to
        reach the bottom-right corner

        Time complexity: O(n^2)
        Space complexity: O(n^2)

        LeetCode: Beats 90.91%
        """
        if obstacleGrid[0][0] == 1:
            return 0

        dp = []

        for _ in range(len(obstacleGrid)):
            dp.append([0] * len(obstacleGrid[0]))

        dp[0][0] = 1

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if obstacleGrid[i][j] != 1:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]
