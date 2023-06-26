class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        A sentence is circular if:

            The last character of a word is equal to the first character of the
            next word.
            The last character of the last word is equal to the first character
            of the first word.

        Given a string sentence, return True if it is circular.
        Otherwise, return False.
        """
        splitted = sentence.split()
        length = len(splitted)

        for i, word in enumerate(splitted):
            if word[-1] != splitted[(i+1) % length][0]:
                return False
        
        return True