class Solution:
    def oddString(self, words: List[str]) -> str:
        """
        You are given an array of equal-length strings words. Assume that the
        length of each string is n.

        Each string words[i] can be converted into a difference integer array
        difference[i] of length n - 1 where
        difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2.
        Note that the difference between two letters is the difference between
        their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1,
        and 'z' is 25.

        For example, for the string "acb",
        the difference integer array is [2 - 0, 1 - 2] = [2, -1].

        All the strings in words have the same difference integer array,
        except one.

        Return the string in words that has different difference integer array.
        """

        # Create hash-table to track differences.
        differences = {}

        for i, word in enumerate(words):
            # Calculate differences array.
            difference = tuple([ord(word[j]) - 97 - (ord(word[j-1]) - 97) for j in range(1, len(word))])

            # There are few possibilities of first 3 values, for example:
            # T, F, F (F, T, F) -> code will return result after 3 iteration in the 2 elif block
            # F, F, T -> code will return result after 3 interation in the 1 elif block
            # F, F, F, ... -> code will return result when meet different difference
            if i < 2:
                if difference not in differences.keys():
                    # {(2, -1): 'acb'}
                    differences[difference] = word

            elif difference not in differences:
                return word
            
            elif len(differences) == 2:
                for diff, w in differences.items():
                    if diff != difference:
                        return w