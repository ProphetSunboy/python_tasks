class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """
        Given an array of strings words and a string chars.

        A string is good if it can be formed by characters from chars (each
        character can only be used once).

        Return the sum of lengths of all good strings in words.
        """
        freqs = {}
        for ch in chars:
            if ch not in freqs:
                freqs[ch] = 1
            else:
                freqs[ch] += 1
        
        sum_len = 0
        for word in words:
            sum_len += len(word)
            for ch in set(word):
                if word.count(ch) > freqs.get(ch, 0):
                    sum_len -= len(word)
                    break

        return sum_len