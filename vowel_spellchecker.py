class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        Implements a spellchecker that, given a wordlist and a list of queries,
        returns the correct spelling for each query according to the following rules:

        1. **Exact Match**: If the query exactly matches a word in the wordlist (case-sensitive), return the query itself.
        2. **Case-Insensitive Match**: If the query matches a word in the wordlist
        ignoring case, return the first such word from the wordlist.
        3. **Vowel Error Match**: If the query matches a word in the wordlist by
        replacing each vowel ('a', 'e', 'i', 'o', 'u') with any other vowel
        (case-insensitive), return the first such word from the wordlist.
        4. **No Match**: If none of the above, return an empty string.

        The precedence is: exact match > case-insensitive match > vowel error match > no match.

        Args:
            wordlist (List[str]): The list of valid words.
            queries (List[str]): The list of query words to check.

        Returns:
            List[str]: A list where each element is the corrected word for the
            corresponding query, or an empty string if no match is found.

        Examples:
            >>> wordlist = ["YellOw"]
            >>> queries = ["yollow", "yeellow", "yllw"]
            >>> spellchecker(wordlist, queries)
            ['YellOw', '', '']

            >>> wordlist = ["yellow", "Yellow"]
            >>> queries = ["YellOw", "yellow"]
            >>> spellchecker(wordlist, queries)
            ['yellow', 'yellow']

        Time Complexity: O(N * Q * L), where N is the length of wordlist, Q is the number of queries, and L is the average word length.
        Space Complexity: O(N * L)
        """
        correct = []

        for q in queries:
            if q in wordlist:
                correct.append(q)
            else:
                word = ""
                word_vowel = ""
                for w in wordlist:
                    if q.lower() == w.lower():
                        word = w
                        break
                    elif len(q) == len(w):
                        flag = True
                        for i in range(len(q)):
                            if q[i].lower() in "aeiou" and w[i].lower() in "aeiou":
                                continue
                            elif q[i].lower() == w[i].lower():
                                continue
                            else:
                                flag = False
                                break

                        if flag and not word_vowel:
                            word_vowel = w

                if word:
                    correct.append(word)
                    continue
                elif word_vowel:
                    correct.append(word_vowel)
                else:
                    correct.append("")

        return correct
