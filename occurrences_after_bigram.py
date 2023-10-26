class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        """
        Given two strings first and second, consider occurrences in some text of
        the form "first second third", where second comes immediately after
        first, and third comes immediately after second.

        Return a list of all the words third for each occurrence of "first
        second third".

        :param str text: string, consisting of lowercase English letters and spaces
        :param str first: string, consisting of lowercase English letters
        :param str second: string, consisting of lowercase English letters
        :returns list[str] thirds: all the words third for each occurrence of
        "first second third"

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.80%
        """
        words = text.split()
        thirds = []

        for i in range(1, len(words) - 1):
            if words[i] == second and words[i - 1] == first:
                thirds.append(words[i + 1])

        return thirds
