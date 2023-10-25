class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        We build a table of n rows (1-indexed). We start by writing 0 in the 1st
        row. Now in every subsequent row, we look at the previous row and
        replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

            For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the
            3rd row is 0110.

        Given two integer n and k, return the kth (1-indexed) symbol in the nth
        row of a table of n rows.

        :param int n: integer number
        :param int k: integer number
        :returns int symbol: kth symbol in the nth row of a table of n rows

        Time complexity: O(logn)
        Space complexity: O(logn)

        LeetCode: Beats 96.91%
        """
        count = bin(k - 1).count("1")
        return 0 if count % 2 == 0 else 1
