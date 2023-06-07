class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Given 3 positives numbers a, b and c. Return the minimum flips required
        in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
        Flip operation consists of change any single bit 1 to 0 or change the
        bit 0 to 1 in their binary representation.

        Constraints:
            1 <= a <= 10^9
            1 <= b <= 10^9
            1 <= c <= 10^9

        """
        # .zfill(30) because len(bin(10 ** 9)) == 30
        bin_a = bin(a)[2:].zfill(30)
        bin_b = bin(b)[2:].zfill(30)
        bin_c = bin(c)[2:].zfill(30)
        
        flips = 0
        for i in range(len(bin_a)):
            if bin_a[i] == '0' and bin_b[i] == '0' and bin_c[i] == '1':
                flips += 1
            elif bin_a[i] == '1' and bin_b[i] == '1' and bin_c[i] == '0':
                flips += 2
            elif (bin_a[i] == '1' or bin_b[i] == '1') and bin_c[i] == '0':
                flips += 1
        
        return flips