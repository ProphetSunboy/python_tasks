class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        Determines if the typed string could be a result of long pressing characters
        while typing the original name string.

        When typing a character, a user might long press a key, causing the same character
        to appear one or more times in a row. This function checks if the string 'typed'
        could be the result of such long presses on the string 'name'.

        Args:
            name (str): The original name string.
            typed (str): The string produced by possibly long pressing some keys.

        Returns:
            bool: True if 'typed' could be a result of long pressing characters in 'name',
            False otherwise.

        Example:
            Input: name = "alex", typed = "aaleex"
            Output: True

            Input: name = "saeed", typed = "ssaaedd"
            Output: False

        Time Complexity: O(N), where N is the length of 'typed'.
        Space Complexity: O(M), where M is the number of unique character groups.

        LeetCode: Beats 100% of submissions
        """

        def group_characters(s: str) -> list[list]:
            prev = s[0]
            prev_c = 1
            s_groups = []

            for i in range(len(s)):
                if s[i] == prev:
                    prev_c += 1
                else:
                    s_groups.append([prev, prev_c])
                    prev = s[i]
                    prev_c = 1

            s_groups.append([prev, prev_c])

            return s_groups

        name_groups = group_characters(name)
        typed_groups = group_characters(typed)

        if len(name_groups) != len(typed_groups):
            return False

        for i in range(len(name_groups)):
            if (
                name_groups[i][0] != typed_groups[i][0]
                or name_groups[i][1] > typed_groups[i][1]
            ):
                return False

        return True
