class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        """
        Calculates the maximum possible average pass ratio after optimally assigning extra students to classes.

        Each class is represented as [pass, total], where pass is the number of students currently passing,
        and total is the total number of students in the class. You are given extraStudents, each of whom
        is guaranteed to pass and can be assigned to any class. The goal is to assign these students to maximize
        the average pass ratio across all classes.

        The pass ratio of a class is defined as (number of passing students) / (total number of students).
        The average pass ratio is the mean of all class pass ratios.

        Args:
            classes (list[list[int]]): A list of classes, each represented as [pass, total].
            extraStudents (int): The number of extra students to assign.

        Returns:
            float: The maximum possible average pass ratio after assignment.

        Example:
            >>> maxAverageRatio([[1,2],[3,5],[2,2]], 2)
            0.78333

        Time Complexity: O((n + extraStudents) * log n), where n is the number of classes.
        Space Complexity: O(n)
        """
        heap = []

        for i, (passed, total) in enumerate(classes):
            ratio_diff = (passed + 1) / (total + 1) - passed / total
            heapq.heappush(heap, (-ratio_diff, i))

        while extraStudents > 0:
            neg_diff, idx = heapq.heappop(heap)
            classes[idx][0] += 1
            classes[idx][1] += 1

            passed, total = classes[idx]
            new_ratio_diff = (passed + 1) / (total + 1) - passed / total

            heapq.heappush(heap, (-new_ratio_diff, idx))

            extraStudents -= 1

        return sum(passed / total for passed, total in classes) / len(classes)
