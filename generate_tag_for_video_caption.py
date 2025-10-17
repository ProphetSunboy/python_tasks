class Solution:
    def generateTag(self, caption: str) -> str:
        """
        Generates a valid video tag from the given caption string.

        The generated tag must:
        - Combine all words in `caption` into a single camelCase string prefixed with '#'.
          - The first word is in lowercase; each subsequent word starts with an uppercase letter, followed by lowercase letters.
        - Remove all characters that are not English letters, except the initial '#'.
        - Truncate the result to a maximum of 100 characters.

        Args:
            caption (str): The input string representing the video caption.

        Returns:
            str: The processed tag string following the rules above.

        Example:
            >>> generateTag("welcome to the 2024 Coding-Challenge!")
            '#welcomeToTheCodingchallenge'

        Time Complexity: O(n), where n is the length of the input string.
        Space Complexity: O(n), for storing processed characters.

        LeetCode: Beats 100% of submissions
        """
        caption = caption.title().lstrip()
        tag = "#"

        if caption:
            tag += caption[0].lower()

        for i in range(1, len(caption)):
            if caption[i].isalpha():
                tag += caption[i]

                if len(tag) == 100:
                    break

        return tag
