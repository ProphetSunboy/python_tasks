class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        Given a positive integer n, construct a 0-indexed list `powers` consisting
        of the minimum number of powers of 2 that sum to n. The list is sorted in
        non-decreasing order, and this representation is unique for each n.

        You are also given a 0-indexed 2D integer list `queries`, where each
        `queries[i] = [left_i, right_i]` specifies a range. For each query, compute
        the product of all `powers[j]` with `left_i <= j <= right_i`.

        Return a list `answers` of length equal to `queries`, where `answers[i]`
        is the answer to the i-th query, modulo 10^9 + 7.

        Args:
            n (int): The integer to be represented as a sum of powers of 2.
            queries (List[List[int]]): Each sublist contains two indices [left, right] specifying the range in the `powers` list.

        Returns:
            List[int]: The product of the specified sublist of `powers` for each query, modulo 10^9 + 7.

        Example:
            productQueries(15, [[0, 1], [2, 2], [0, 3]])
            [2, 4, 64]

        Time Complexity: O(Q * K), where Q is the number of queries and K is the maximum length of a query range.
        Space Complexity: O(log n), for storing the powers of 2 that sum to n.
        """
        powers = []
        pows = []

        for i in range(0, 32):
            if 2**i <= n:
                pows.append(2**i)

        for i in range(len(pows) - 1, -1, -1):
            if n - pows[i] >= 0:
                powers.append(pows[i])
                n -= pows[i]

        powers = powers[::-1]

        answers = []
        for q in queries:
            curr_prod = 1
            for i in range(q[0], q[1] + 1):
                curr_prod *= powers[i]

            answers.append(curr_prod % (10**9 + 7))

        return answers
