class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """Finds the lexicographically smallest equivalent string based on character equivalency rules.

        Given two strings s1 and s2 of equal length, characters at corresponding positions are considered equivalent.
        These equivalencies follow standard equivalence relation rules (reflexivity, symmetry, transitivity).

        Args:
            s1 (str): First string defining character equivalencies
            s2 (str): Second string defining character equivalencies
            baseStr (str): String to find smallest equivalent for

        Returns:
            str: Lexicographically smallest equivalent string of baseStr

        Example:
            >>> smallestEquivalentString("abc", "cde", "eed")
            "aab"  # 'a'=='c', 'b'=='d', 'c'=='e' implies 'e'=='a', so "eed" -> "aab"

        Time complexity: O(n * m) where n is length of baseStr and m is number of unique characters
        Space complexity: O(m) where m is number of unique characters
        """
        vocab = dict()
        result = ""
        eq_d = dict()

        for ch1, ch2 in zip(s1, s2):
            if vocab.get(ch1, 0):
                vocab[ch1].append(ch2)
            else:
                vocab[ch1] = [ch2]

            if vocab.get(ch2, 0):
                vocab[ch2].append(ch1)
            else:
                vocab[ch2] = [ch1]

        for ch in baseStr:
            if eq_d.get(ch, 0):
                result += eq_d.get(ch)
                continue

            eq = vocab.get(ch, [ch])
            available = []
            seen = set()
            smallest = min(eq)
            while eq:
                available = []
                for l in eq:
                    seen.add(l)
                    if l < smallest:
                        smallest = l

                    for c in vocab.get(l, [l]):
                        if c not in seen:
                            available.append(c)
                        if c < smallest:
                            smallest = c

                eq = available

            eq_d[ch] = smallest
            result += smallest

        return result
