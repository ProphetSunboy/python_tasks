class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        """
        Given a 2D integer list intervals, where intervals[i] = [start_i, end_i]
        represents all the integers from start_i to end_i inclusive,
        find the minimum size of a set such that each interval contains at least
        two elements from this set.

        A containing set is a list nums in which every interval from intervals
        has at least two numbers from nums.

        Args:
            intervals (List[List[int]]): List of intervals, where each interval
            is represented as [start, end].

        Returns:
            int: The minimum possible size of a containing set that covers every
            interval with at least two integers.

        Example:
            Input: intervals = [[1,3], [3,7], [8,9]]
            Output: 5
            Explanation: [2,3,4,8,9] would be valid minimal set.

        Time Complexity: O(n log n), where n is the number of intervals (due to sorting).
        Space Complexity: O(1), in addition to the input and output.
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a, b = -1, -1
        count = 0

        for l, r in intervals:
            in_interval = (a >= l) + (b >= l)

            if in_interval == 2:
                continue

            if in_interval == 1:
                count += 1
                a = b
                b = r
            else:
                count += 2
                a = r - 1
                b = r

        return count
