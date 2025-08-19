class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Calculates the minimum number of key pushes required to type a given word on a remappable telephone keypad.

        Each key (2-9) can be mapped to any number of distinct lowercase English letters,
        and each letter must be assigned to exactly one key. To type a letter, you press
        its key as many times as its position in the key's letter list
        (e.g., first letter: 1 push, second letter: 2 pushes, etc.).

        The function finds the optimal mapping to minimize the total number of pushes needed to type the input word.

        Args:
            word (str): A string of distinct lowercase English letters.

        Returns:
            int: The minimum total number of key pushes required to type the word.

        Example:
            >>> minimumPushes("abcde")
            5

        Time Complexity: O(n), where n is the length of word.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        button = 0
        minimum_p = 0
        curr_push = 1

        for ch in word:
            if button <= 7:
                minimum_p += curr_push
                button += 1
            else:
                button = 1
                curr_push += 1
                minimum_p += curr_push

        return minimum_p
