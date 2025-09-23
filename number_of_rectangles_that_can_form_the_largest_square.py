class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        """
        Given a list of rectangles, where rectangles[i] = [l, w] represents the ith rectangle's length and width,
        determine how many rectangles can form the largest possible square.

        For each rectangle, you can cut it to form a square with side length k, where k <= l and k <= w.
        The largest square you can obtain from a rectangle is of side length min(l, w).

        Let maxLen be the maximum side length of a square that can be obtained from any rectangle in the list.
        Return the number of rectangles that can form a square of side length maxLen.

        Args:
            rectangles (List[List[int]]): List of rectangles, each defined by [length, width].

        Returns:
            int: Number of rectangles that can form a square of side length maxLen.

        Example:
            >>> rectangles = [[5,8],[3,9],[5,12],[16,5]]
            >>> countGoodRectangles(rectangles)
            3
            # The largest square has side length 5, and 3 rectangles can form such a square.

        Time Complexity: O(n), where n is the number of rectangles.
        Space Complexity: O(n)

        LeetCode: Beats 97.10% of submissions
        """
        squares = defaultdict(int)

        max_len = 0
        for i, rect in enumerate(rectangles):
            curr_len = min(rect)
            squares[curr_len] += 1

            if curr_len > max_len:
                max_len = curr_len

        return squares[max_len]
