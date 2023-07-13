class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        """
        International Morse Code defines a standard encoding where each letter
        is mapped to a series of dots and dashes, as follows:

            'a' maps to ".-",
            'b' maps to "-...",
            'c' maps to "-.-.", and so on.

        Given an array of strings words where each word can be written as a
        concatenation of the Morse code of each letter.

            For example, "cab" can be written as "-.-..--...", which is the
            concatenation of "-.-.", ".-", and "-...". We will call such a
            concatenation the transformation of a word.

        Return the number of different transformations among all words we have.

        LeetCode: Beats 96.39%
        """
        morse = [
                 ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                 "..-","...-",".--","-..-","-.--","--.."
                ]

        res = set()
        
        for word in words:
            morse_s = ''
            for ch in word:
                morse_s += morse[ord(ch)-97]
            res.add(morse_s)

        return len(res)