class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Given a sorted list of characters `letters` and a target character `target`,
        return the smallest character in `letters` that is lexicographically greater
        than `target`. If no such character exists, return the first character in `letters`.

        Args:
            letters (List[str]): Sorted list of characters (non-decreasing order).
            target (str): A target character.

        Returns:
            str: The smallest character in `letters` greater than `target`,
                or the first character if no such character exists.

        Example:
            Input: letters = ["c", "f", "j"], target = "a"
            Output: "c"

            Input: letters = ["c", "f", "j"], target = "j"
            Output: "c"

        Time Complexity: O(N), where N is the length of letters.
        Space Complexity: O(1)

         LeetCode: Beats 100% of submissions
        """
        letters_set = set(letters)

        curr = ord(target) + 1
        while curr <= 122:
            if chr(curr) in letters_set:
                return chr(curr)

            curr += 1

        return letters[0]
