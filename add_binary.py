class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Given two binary strings a and b, return their sum as a binary string.
        """
        return bin(int(a, 2) + int(b, 2))[2:]