class Solution:
    def capitalizeTitle(self, title: str) -> str:
        """Capitalizes the given title string according to the following rules:
            - If a word has 1 or 2 letters, convert all its letters to lowercase.
            - If a word has 3 or more letters, capitalize the first letter and convert the rest to lowercase.

        Args:
            title (str): The input string consisting of one or more words separated by a single space.

        Returns:
            str: The capitalized title string.

        Example:
            >>> capitalizeTitle("capiTalIze tHe titLe")
            'Capitalize The Title'
            >>> capitalizeTitle("First leTTeR of EACH Word")
            'First Letter of Each Word'

        Time complexity: O(n), where n is the length of the title.
        Space complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        words = title.split()

        for i in range(len(words)):
            if len(words[i]) < 3:
                words[i] = words[i].lower()
            else:
                words[i] = words[i].title()

        return " ".join(words)
