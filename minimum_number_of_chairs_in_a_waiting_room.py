class Solution:
    def minimumChairs(self, s: str) -> int:
        """
        Calculates the minimum number of chairs required in a waiting room based on a sequence of events.

        Each character in the input string `s` represents an event at each second:
            - 'E': A person enters the waiting room and occupies a chair.
            - 'L': A person leaves the waiting room, freeing up a chair.

        The function returns the minimum number of chairs needed so that every
        person who enters always has a chair available, assuming the room is initially empty.

        Args:
            s (str): A string consisting of characters 'E' and 'L' representing entry and leaving events.

        Returns:
            int: The minimum number of chairs required.

        Example:
            >>> minimumChairs("ELEEL")
            2

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        max_chairs = 0
        curr_chairs = 0

        for ch in s:
            if ch == "E":
                curr_chairs += 1

                if curr_chairs > max_chairs:
                    max_chairs = curr_chairs
            else:
                curr_chairs -= 1

        return max_chairs
