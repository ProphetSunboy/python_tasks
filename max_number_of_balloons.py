class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Given a string text, you want to use the characters of text to form as
        many instances of the word "balloon" as possible.

        You can use each character in text at most once. Return the maximum
        number of instances that can be formed.

        LeetCode: Beats 96.26%
        """
        freqs = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for ch in text:
            if ch in freqs:
                freqs[ch] += 1

        freqs['l'] //= 2
        freqs['o'] //= 2

        return min(val for val in freqs.values())