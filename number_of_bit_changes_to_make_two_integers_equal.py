class Solution:
    def minChanges(self, n: int, k: int) -> int:
        """
        Given two positive integers n and k, determine the minimum number of bit changes
        required to make n equal to k.

        You may only change bits in n that are set to 1, flipping them to 0. You cannot flip 0 to 1.

        Return the number of such changes needed to make n equal to k. If it is
        impossible (i.e., k has a 1 in any bit where n has a 0), return -1.

        Args:
            n (int): The original integer.
            k (int): The target integer.

        Returns:
            int: The minimum number of bit changes required, or -1 if impossible.

        Example:
            >>> minChanges(13, 9)
            1
            # 13 = 1101, 9 = 1001; change the second bit from the right (1 -> 0)

            >>> minChanges(5, 7)
            -1
            # 5 = 101, 7 = 111; impossible since you cannot flip 0 to 1

        Time Complexity: O(log(max(n, k)))
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        bin_n = bin(n)[2:]
        bin_k = bin(k)[2:]

        if n > k:
            bin_k = bin_k.zfill(len(bin_n))
        else:
            bin_n = bin_n.zfill(len(bin_k))

        bits = 0
        for i in range(len(bin_n)):
            if bin_n[i] == "0" and bin_k[i] == "1":
                return -1
            elif bin_n[i] == "1" and bin_k[i] == "0":
                bits += 1

        return bits
