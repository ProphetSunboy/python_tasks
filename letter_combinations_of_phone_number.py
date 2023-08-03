class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Given a string containing digits from 2-9 inclusive, return all possible
        letter combinations that the number could represent.
        Return the answer in any order.

        :param str digits: string, containing numbers
        :returns list[str] combs: list, containing all possible letter combinations

        Time complexity: O(4^n)
        Space complexity: O(n)

        LeetCode: Beats 99.26%
        """
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combs = []

        def combine(comb, digits):
            if len(digits) == 0:
                combs.append(comb)
            else:
                for ch in mapping[digits[0]]:
                    combine(comb + ch, digits[1:])

        combine("", digits)

        return combs
