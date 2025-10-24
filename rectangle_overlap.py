class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        Determine if two axis-aligned rectangles overlap.

        Each rectangle is represented as a list [x1, y1, x2, y2], where:
            - (x1, y1): coordinates of the bottom-left corner
            - (x2, y2): coordinates of the top-right corner

        Two rectangles overlap if their intersection has a positive area.
        Rectangles that only touch at edges or corners do not overlap.

        Args:
            rec1 (List[int]): [x1, y1, x2, y2] for the first rectangle
            rec2 (List[int]): [x1, y1, x2, y2] for the second rectangle

        Returns:
            bool: True if the rectangles overlap, False otherwise

        Example:
            >>> isRectangleOverlap([0,0,2,2], [1,1,3,3])
            True
            >>> isRectangleOverlap([0,0,1,1], [1,1,2,2])
            False

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return not (
            rec1[2] <= rec2[0]
            or rec1[0] >= rec2[2]
            or rec1[3] <= rec2[1]
            or rec1[1] >= rec2[3]
        )
