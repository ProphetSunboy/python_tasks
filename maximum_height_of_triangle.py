class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        """
        Given two integers, red and blue, representing the number of red and blue balls respectively,
        arrange the balls to form a triangle such that:
            - The 1st row has 1 ball, the 2nd row has 2 balls, the 3rd row has 3 balls, and so on.
            - All balls in a row are the same color.
            - Adjacent rows must have different colors.

        Returns the maximum possible height of such a triangle.

        Args:
            red (int): Number of red balls.
            blue (int): Number of blue balls.

        Returns:
            int: The maximum height of the triangle that can be formed.

        Example:
            >>> maxHeightOfTriangle(5, 6)
            4

        Time Complexity: O(sqrt(n)), where n = red + blue (since the number of rows is bounded by the sum of balls).
        Space Complexity: O(1)

        LeetCode: Beats 95.18% of submissions
        """
        max_height = 0

        for i in range(2):
            curr_r = bool(i)
            r, b = red, blue
            curr_height = 0
            row = 1

            while r > 0 or b > 0:
                if curr_r:
                    if r - row < 0:
                        break
                    r -= row
                    curr_r = False
                else:
                    if b - row < 0:
                        break
                    b -= row
                    curr_r = True

                curr_height += 1
                row += 1

            if curr_height > max_height:
                max_height = curr_height

        return max_height
