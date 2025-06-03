class Solution:
    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int],
    ) -> int:
        """Given n boxes labeled from 0 to n-1, find the maximum candies you can collect.

        Args:
            status (list[int]): status[i] is 1 if box i is open, 0 if closed
            candies (list[int]): candies[i] is number of candies in box i
            keys (list[list[int]]): keys[i] contains box labels that can be opened after opening box i
            containedBoxes (list[list[int]]): containedBoxes[i] contains boxes found inside box i
            initialBoxes (list[int]): Labels of boxes you start with

        Returns:
            int: Maximum number of candies that can be collected

        Example:
            >>> maxCandies([1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]],[0,1,2,3])
            16

        Time complexity: O(n) where n is the number of boxes
        Space complexity: O(n) for storing available boxes dictionary

        LeetCode: Beats 100% of submissions
        """
        available_boxes = dict()
        max_candies = 0
        for box in initialBoxes:
            available_boxes[box] = 1

        while available_boxes:
            opened_boxes = []
            new_boxes = []
            for box in available_boxes.keys():
                if status[box]:
                    max_candies += candies[box]
                    for key in keys[box]:
                        status[key] = 1
                    for contained_box in containedBoxes[box]:
                        new_boxes.append(contained_box)

                    opened_boxes.append(box)

            if not opened_boxes:
                break

            for box in opened_boxes:
                available_boxes.pop(box)

            for box in new_boxes:
                available_boxes[box] = 1

        return max_candies
