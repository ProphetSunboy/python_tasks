class Solution:
    def modifyString(self, s: str) -> str:
        """
        Replaces all '?' characters in the input string `s` with lowercase English letters so that
        the resulting string contains no consecutive repeating characters. Non-'?' characters are not modified.

        It is guaranteed that the input string does not contain consecutive repeating characters,
        except possibly for '?'.

        If there are multiple valid solutions, any one of them may be returned. An answer is always possible.

        Args:
            s (str): The input string containing lowercase English letters and/or '?'.

        Returns:
            str: The modified string with all '?' replaced and no consecutive repeating characters.

        Example:
            >>> modifyString("a?b?")
            'acba'  # or any valid string with no consecutive repeating characters

        Time Complexity: O(n), where n is the length of the input string.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissionss
        """
        res = ""

        if s[0] != "?":
            res += s[0]
        elif len(s) > 1:
            if s[1] != "a":
                res += "a"
            else:
                res += "b"
        else:
            res += "a"

        for i in range(1, len(s)):
            if s[i] == "?":
                if i + 1 < len(s):
                    if res[-1] == "a":
                        if s[i + 1] == "b":
                            res += "c"
                        else:
                            res += "b"
                    else:
                        if s[i + 1] == "a":
                            if res[-1] == "b":
                                res += "c"
                            else:
                                res += "b"
                        else:
                            res += "a"
                else:
                    if res[-1] == "a":
                        res += "b"
                    else:
                        res += "a"
            else:
                res += s[i]

        return res
