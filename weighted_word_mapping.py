class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        """
        Given a list of words and a list of letter weights, maps each word to a
        letter based on the sum of its character weights.

        For each word, calculate the sum of weights for its characters, take this
        sum modulo 26, and map the result to a lowercase English letter using
        reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a'). The final
        result is the concatenation of these mapped characters for all words.

        Args:
            words (List[str]): List of words consisting of lowercase English letters.
            weights (List[int]): List of 26 integers, where weights[i] is the weight
                of the i-th lowercase English letter ('a' to 'z').

        Returns:
            str: String formed by concatenating the mapped characters for all words
                in order.

        Example:
            Input: words = ["abcd","def","xyz"],
            weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

            Output: "rij"

        Time Complexity: O(W * L), where W is the number of words and L is the
        average word length, since each character of every word is processed once.
        Space Complexity: O(1), since the result string uses O(W) space for
        output and no extra space proportional to input size is used.

        LeetCode: Beats 98.39% of submissions
        """
        res = ""

        for word in words:
            curr = sum([weights[ord(ch) - 97] for ch in word]) % 26

            res += chr(122 - curr)

        return res
