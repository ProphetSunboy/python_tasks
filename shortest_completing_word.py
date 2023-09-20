class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        """
        Given a string licensePlate and a list of strings words, find the
        shortest completing word in words.

        A completing word is a word that contains all the letters in
        licensePlate. Ignore numbers and spaces in licensePlate, and treat
        letters as case insensitive. If a letter appears more than once in
        licensePlate, then it must appear in the word the same number of times
        or more.

        For example, if licensePlate = "aBc 12c", then it contains letters 'a',
        'b' (ignoring case), and 'c' twice. Possible completing words are
        "abccdef", "caaacab", and "cbca".

        Return the shortest completing word in words. It is guaranteed an answer
        exists. If there are multiple shortest completing words, return the
        first one that occurs in words.

        :param str licensePlate: string
        :param list[str] words: list of strings
        :returns str completing_word: word that contains all the letters in
        licensePlate

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 98.06%
        """
        letters = {}

        for l in licensePlate.lower():
            if l.isalpha():
                letters[l] = letters.get(l, 0) + 1

        words.sort(key=len)
        for word in words:
            w = collections.Counter(word)
            complete = True

            for key, val in letters.items():
                if val > w[key]:
                    complete = False
                    break

            if complete:
                return word
