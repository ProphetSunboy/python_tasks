class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Returns the minimum time required to make the rope colorful by removing balloons.

        Alice has n balloons in a row, described by the string `colors` where `colors[i]` is the color of the ith balloon.
        She wants the rope to be "colorful", meaning no two consecutive balloons are of the same color.
        Bob can remove any balloons: removing the ith balloon takes `neededTime[i]` seconds.
        Find the minimum total removal time required so that no two consecutive balloons have the same color.

        Args:
            colors (str): A string of length n representing the color of each balloon.
            neededTime (List[int]): A list of integers where neededTime[i] is the removal time for the ith balloon.

        Returns:
            int: The minimum total time required to make the rope colorful.

        Example:
            >>> minCost("abaac", [1,2,3,4,5])
            3

            >>> minCost("abc", [1,2,3])
            0

            >>> minCost("aabaa", [1,2,3,4,1])
            2

        Time Complexity: O(n), where n is the length of the colors string.
        Space Complexity: O(1), beyond the input and output.

        LeetCode: Beats 91.47% of submissions
        """
        curr_colors = [colors[0]]
        curr_time_needed = [neededTime[0]]
        min_time = 0

        for i in range(1, len(colors)):
            if curr_colors[-1] == colors[i]:
                if neededTime[i] <= curr_time_needed[-1]:
                    min_time += neededTime[i]
                else:
                    min_time += curr_time_needed.pop()
                    curr_time_needed.append(neededTime[i])
            else:
                curr_colors.append(colors[i])
                curr_time_needed.append(neededTime[i])

        return min_time
