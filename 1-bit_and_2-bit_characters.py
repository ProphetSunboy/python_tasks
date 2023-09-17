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
        last_chr = 1

        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                res = 1
            else:
                i += 1
                res = 0

        return res == 0
