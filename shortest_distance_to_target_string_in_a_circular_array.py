class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        """
        Finds the shortest distance to reach a target string in a circular list.

        You are given a 0-indexed circular string list words and a string target. A circular
        list means that the list's end connects to the list's beginning.

        Formally, the next element of words[i] is words[(i + 1) % n] and the previous element
        of words[i] is words[(i - 1 + n) % n], where n is the length of words.
        Starting from startIndex, you can move to either the next word or the previous word
        with 1 step at a time.

        Args:
            words (List[str]): A circular list of strings to search through.
            target (str): The target string to find.
            startIndex (int): The starting index in the circular list.

        Returns:
            int: The shortest distance needed to reach the string target.
                 Returns -1 if the string target does not exist in words.

        Examples:
            >>> closestTarget(["hello", "world", "hello"], "world", 0)
            1
            >>> closestTarget(["a", "b", "c"], "d", 0)
            -1
            >>> closestTarget(["hello", "world", "hello"], "hello", 1)
            1

        Time Complexity: O(n) where n is the length of words
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        shortest = len(words)

        i = startIndex
        dist = 0
        while words[i] != target:
            i = (i + 1) % len(words)
            dist += 1

            if dist == len(words):
                return -1

        shortest = dist
        i = startIndex
        dist = 0
        while words[i] != target:
            i = (i - 1 + len(words)) % len(words)
            dist += 1

        if dist < shortest:
            shortest = dist

        return shortest
