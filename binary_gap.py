class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Given a positive integer n, find and return the longest distance between
        any two adjacent 1's in the binary representation of n. If there are no
        two adjacent 1's, return 0.

        Two 1's are adjacent if there are only 0's separating them
        (possibly no 0's). The distance between two 1's is the absolute
        difference between their bit positions. For example, the two 1's in
        "1001" have a distance of 3.

        :param int n: positive integer
        :returns int longest_gap: longest distance between any two adjacent 1's
        in the binary representation of n

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 94.89%
        """
        longest_gap = 0
        start = 0

        b = bin(n)[2:]

        for i in range(len(b)):
            if b[i] == "1":
                if i - start > longest_gap:
                    longest_gap = i - start

                start = i

        return longest_gap
