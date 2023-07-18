class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Write a function that takes the binary representation of an unsigned
        integer and returns the number of '1' bits it has (also known as the
        Hamming weight).
        """
        bits = 0
        
        for bit in bin(n)[2:]:
            if bit == '1':
                bits += 1

        return bits