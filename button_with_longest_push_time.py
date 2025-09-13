class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        """
        Given a 2D list `events` representing a sequence of button presses, where each
        `events[i] = [index_i, time_i]` indicates that the button at index `index_i` was
        pressed at time `time_i` (with the list sorted by increasing time):

        - The time taken to press a button is the difference in time between consecutive
          button presses. For the first button, the time is simply the time at which it
          was pressed.
        - Return the index of the button that took the longest time to push. If multiple
          buttons have the same longest time, return the button with the smallest index.

        Args:
            events (List[List[int]]): A list of [index, time] pairs representing button presses.

        Returns:
            int: The index of the button with the longest push time. If there are ties,
                 returns the smallest such index.

        Example:
            >>> buttonWithLongestTime([[0,2],[1,5],[0,9],[2,15]])
            2

        Time Complexity: O(n), where n is the number of events.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        longest = events[0][1]
        longest_idx = events[0][0]

        for i in range(1, len(events)):
            if events[i][1] - events[i - 1][1] > longest:
                longest = events[i][1] - events[i - 1][1]
                longest_idx = events[i][0]
            elif (
                events[i][1] - events[i - 1][1] == longest
                and events[i][0] < longest_idx
            ):
                longest_idx = events[i][0]

        return longest_idx
