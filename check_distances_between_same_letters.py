class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        """
        Checks if the given string s is a well-spaced string according to the provided distance list.

        A well-spaced string is defined as a string where each lowercase English letter appears exactly twice,
        and the number of letters between the two occurrences of the ith letter is equal to distance[i], where
        i is the 0-based index of the letter ('a' -> 0, 'b' -> 1, ..., 'z' -> 25).

        Args:
            s (str): A 0-indexed string consisting of only lowercase English letters, each appearing exactly twice.
            distance (list[int]): A list of 26 integers where distance[i] is the required number of letters between
                                  the two occurrences of the ith letter.

        Returns:
            bool: True if s is a well-spaced string, False otherwise.

        Example:
            >>> checkDistances("abaccb", [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            True

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        seen = set()

        for i in range(len(s)):
            dist = distance[ord(s[i]) - 97]

            if s[i] not in seen:
                if i + dist + 1 >= len(s):
                    return False
                elif s[i] != s[i + dist + 1]:
                    return False

                seen.add(s[i])

        return True
