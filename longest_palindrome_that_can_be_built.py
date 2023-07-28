import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Given a string s which consists of lowercase or uppercase letters,
        return the length of the longest palindrome that can be built with those
        letters.

        Letters are case sensitive, for example, "Aa" is not considered a
        palindrome here.

        Time complexity: O(2n)
        Space complexity: O(n)

        LeetCode: Beats 99.89%
        """
        count = collections.Counter(s)
        palindrome = 0
        odd = False

        for val in count.values():
            if not odd and val % 2:
                palindrome += val
                odd = True
            else:
                palindrome += val

                if val % 2:
                    palindrome -= 1

        return palindrome
