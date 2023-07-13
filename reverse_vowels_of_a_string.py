class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Given a string s, reverse only all the vowels in the string and
        return it.

        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
        lower and upper cases, more than once.

        LeetCode: Beats 97.25%
        """
        res = [''] * len(s)
        vowels = 'aeiouAEIOU'

        left, right = 0, len(s)-1

        while left <= right:
            if s[left] not in vowels:
                res[left] = s[left]
                left += 1
            else:
                while s[right] not in vowels:
                    res[right] = s[right]
                    right -= 1

                res[left], res[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(res)