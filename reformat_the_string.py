class Solution:
    def reformat(self, s: str) -> str:
        """
        You are given an alphanumeric string s. (Alphanumeric string is a string
        consisting of lowercase English letters and digits).

        You have to find a permutation of the string where no letter is followed
        by another letter and no digit is followed by another digit. That is, no
        two adjacent characters have the same type.

        Return the reformatted string or return an empty string if it is
        impossible to reformat the string.

        :param str s: alphanumeric string
        :returns str: reformatted string or an empty string if it is impossible
        to reformat the string

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 94.77%
        """
        nums = []
        letters = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                nums.append(ch)

        if abs(len(nums) - len(letters)) > 1:
            return ''

        if len(nums) > len(letters):
            return ''.join([nums.pop() if i % 2 == 0 else letters.pop() for i in range(len(s))])
        
        return ''.join([letters.pop() if i % 2 == 0 else nums.pop() for i in range(len(s))])