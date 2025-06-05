class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        vocab = dict()
        result = ""

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
            eq = vocab.get(ch, [ch])
            smallest = min(eq)
            for l in eq:
                if min(vocab.get(l, [l])) < smallest:
                    smallest = min(vocab.get(l))

            result += smallest

        return result


a = Solution()
print(a.smallestEquivalentString(s1="leetcode", s2="programs", baseStr="sourcecode"))
