class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        """Determines the key with the longest keypress duration from a sequence of keypresses.

        Args:
            releaseTimes (list[int]): A list where releaseTimes[i] is the time the ith key was released.
            keysPressed (str): A string where keysPressed[i] is the ith key pressed.

        Returns:
            str: The key with the longest keypress duration. If multiple keys have the same duration,
                 returns the lexicographically largest key.

        The duration of the 0th keypress is releaseTimes[0]. For i > 0, the duration is releaseTimes[i] - releaseTimes[i-1].

        Example:
            >>> slowestKey([9,29,49,50], "cbcd")
            'c'

        Time complexity: O(n), where n is the length of keysPressed.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        key_duration = {keysPressed[0]: releaseTimes[0]}
        longest = releaseTimes[0]
        longest_key = keysPressed[0]

        for i in range(1, len(keysPressed)):
            curr = releaseTimes[i] - releaseTimes[i - 1]

            if key_duration.get(keysPressed[i], 0) < curr:
                key_duration[keysPressed[i]] = curr

            if curr > longest:
                longest = curr
                longest_key = keysPressed[i]
            elif curr == longest and keysPressed[i] > longest_key:
                longest = curr
                longest_key = keysPressed[i]

        return longest_key
