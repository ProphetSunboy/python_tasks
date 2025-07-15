class Solution:
    def isValid(self, word: str) -> bool:
        """Determines if a given word is valid based on the following criteria:
            - The word must be at least 3 characters long.
            - The word must contain only digits (0-9) and English letters (uppercase or lowercase).
            - The word must include at least one vowel ('a', 'e', 'i', 'o', 'u', case-insensitive).
            - The word must include at least one consonant (an English letter that is not a vowel).

        Args:
            word (str): The word to validate.

        Returns:
            bool: True if the word is valid, False otherwise.

        Examples:
            >>> isValid("abc")
            True
            >>> isValid("a1e")
            False
            >>> isValid("aei")
            False
            >>> isValid("bcd")
            False

        Time complexity: O(n), where n is the length of the word.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        if len(word) < 3:
            return False

        vowels = {"a", "e", "i", "o", "u"}
        validation = {"vowel": False, "consonant": False}
        password = word.lower()

        for ch in password:
            if not ch.isalnum():
                return False
            elif ch in vowels:
                validation["vowel"] = True
            elif ch.isalpha():
                validation["consonant"] = True

        return all(validation.values())
