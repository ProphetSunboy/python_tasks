class Solution:
    def all_equal(self, lst):
        """
        Checks if all elements of given list lst is equal.
        """
        num = lst[0]
        g = lambda x: x == num
        return all(map(g, lst))

    def equalFrequency(self, word: str) -> bool:
        """
        Given a 0-indexed string word, consisting of lowercase English letters.
        Select one index and remove the letter at that index from word so that
        the frequency of every letter present in word is equal.

        Return true if it is possible to remove one letter so that the frequency
        of all letters in word are equal, and false otherwise.
        """
        freqs = [word.count(ch) for ch in set(word)]
        if freqs.count(1) == 1 or freqs.count(1) == len(freqs):
            freqs.remove(1)
            return self.all_equal(freqs)
        else:
            freqs[freqs.index(max(freqs))] -= 1
            return self.all_equal(freqs)