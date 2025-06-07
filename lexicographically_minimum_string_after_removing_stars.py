class Solution:
    def clearStars(self, s: str) -> str:
        """Removes all '*' characters from a string by repeatedly removing the leftmost '*' and the smallest character to its left.

        For each '*' encountered, the algorithm removes both the '*' and the lexicographically smallest
        non-'*' character that appears before it. If multiple smallest characters exist, any can be chosen.

        Args:
            s (str): Input string that may contain '*' characters

        Returns:
            str: The resulting string after removing all '*' characters and their corresponding smallest
                 characters to the left

        Example:
            >>> clearStars("a*b*c")
            'c'
            >>> clearStars("abc*")
            'bc'

        Time complexity: O(n²) - where n is the length of the string, as we may need to scan backwards
                         for each '*' encountered
        Space complexity: O(n) - for storing the list representation of the string
        """
        res = ""
        l = list(s)

        for i, ch in enumerate(s):
            if ch == "*":
                l[i] = "{"

                smallest = l[i - 1]
                idx = i - 1
                for j in range(i - 2, -1, -1):
                    if l[j] < smallest:
                        smallest = l[j]
                        idx = j

                l[idx] = "{"

        for ch in l:
            if ch != "{":
                res += ch

        return res
