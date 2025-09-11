class Solution:
    def sortVowels(self, s: str) -> str:
        """
        Given a 0-indexed string s, return a new string t where:
            - All consonants remain in their original positions.
            - All vowels ('a', 'e', 'i', 'o', 'u', both lowercase and uppercase) are sorted
            in nondecreasing order of their ASCII values, but remain in their original positions among the consonants.

        Args:
            s (str): The input string.

        Returns:
            str: The resulting string with vowels sorted and consonants unchanged.

        Example:
            >>> sortVowels("lEetcOde")
            'lEOtcede'

        Time Complexity: O(n log n), where n is the length of s (due to sorting the vowels).
        Space Complexity: O(n)

        LeetCode: Beats 91.12% of submissions
        """
        t = [0] * len(s)
        vowels = []
        vowels_idx = []

        for i, ch in enumerate(s):
            if ch in "aeiouAEIOU":
                vowels.append(ch)
                vowels_idx.append(i)
            else:
                t[i] = ch

        vowels.sort(reverse=True)
        for i in vowels_idx:
            t[i] = vowels.pop()

        return "".join(t)
