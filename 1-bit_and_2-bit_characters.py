# First solution
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        """
        Given a binary list bits that ends with 0, return True if the last
        character must be a one-bit character.

        There are two special characters:

            The first character can be represented by one bit 0.
            The second character can be represented by two bits (10 or 11).

        :param list[int] bits: binary list
        :returns bool last_chr: last character must be a one-bit character

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 98.97%
        """
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                res = 1
            else:
                i += 1
                res = 0

        return res == 0


# Second solution
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        Determines if the last character in the bits list must be a one-bit character.

        There are two types of characters:
            - A one-bit character represented by a single '0'.
            - A two-bit character represented by '10' or '11'.

        Given a binary list 'bits' that always ends with 0, return True if the
        last character must be a one-bit character.

        Args:
            bits (List[int]): The input binary list ending with 0.

        Returns:
            bool: True if the last character is necessarily a one-bit character, False otherwise.

        Example:
            Input: bits = [1, 0, 0]
            Output: True

        Time Complexity: O(n), where n is the length of bits.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2

        return i == len(bits) - 1
