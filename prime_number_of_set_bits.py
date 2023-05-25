class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Given two integers left and right, return the count of numbers in
        the inclusive range [left, right] having a prime number of set bits
        in their binary representation.

        Number of set bits an integer has is the number of 1's
        present when written in binary.
        """
        counter = 0
        for num in range(left, right+1):
            if bin(num)[2:].count('1') in {2,3,5,7,11,13,17,19}:
                counter += 1
        return counter