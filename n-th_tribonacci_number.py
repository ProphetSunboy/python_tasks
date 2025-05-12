class Solution:
    def tribonacci(self, n: int) -> int:
        """
        The Tribonacci sequence Tn is defined as follows: 
        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
        Given n, return the value of Tn.
        """
        if n == 0:
            return 0

        seq = [0, 1, 1]
        for i in range(3, n+1):
            seq.append(seq[i-1] + seq[i-2] + seq[i-3])

        return seq[-1]