# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         s =  paragraph.translate(str.maketrans("!?',;.", '      '))
#         freqs = {}

#         max_freq = 0
#         w = ''
#         for word in s.lower().split():
#             if word not in banned:
#                 if word in freqs:
#                     freqs[word] += 1
#                 else:
#                     freqs[word] = 1

#                 if freqs[word] > max_freq:
#                     w = word
#                     max_freq = freqs[word]
            
#         return w


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        Given a string paragraph and a string array of the banned words banned,
        return the most frequent word that is not banned. It is guaranteed there
        is at least one word that is not banned, and that the answer is unique.

        The words in paragraph are case-insensitive and the answer should be
        returned in lowercase.
        """
        s =  paragraph.translate(str.maketrans("!?',;.", '      '))
        freqs = {}

        for word in s.lower().split():
            if word not in banned:
                if word in freqs:
                    freqs[word] += 1
                else:
                    freqs[word] = 1

        max_freq = 0
        w = ''
        for key, val in freqs.items():
            if val > max_freq:
                w = key
                max_freq = val

        return w