class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        """Decodes a message using a substitution cipher based on a given key.

        Given a key string and a message string, creates a substitution table using the first
        appearance of each lowercase letter in the key, then uses this table to decode the message.
        Spaces remain unchanged.

        Args:
            key (str): The cipher key containing all 26 lowercase English letters
            message (str): The encoded message to decode

        Returns:
            str: The decoded message

        Example:
            >>> decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv")
            'this is a secret'

        Time complexity: O(n + m) - where n is length of key and m is length of message
        Space complexity: O(1) - fixed size dictionary for substitution table

        LeetCode: Beats 100% of submissions
        """
        vocab = {" ": " "}
        next_letter_ord = 97
        decoded_message = ""

        for ch in key:
            if vocab.get(ch, 0) == 0:
                vocab[ch] = chr(next_letter_ord)
                next_letter_ord += 1

        for ch in message:
            decoded_message += vocab[ch]

        return decoded_message
