class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        """
        Counts the number of valid unlock order permutations for computers given
        their password complexities.

        There are n computers labeled from 0 to n - 1, each with a password of complexity[i].
        - Computer 0's password is already decrypted ("root").
        - To unlock computer i (>0), you must have previously unlocked some
        computer j (j < i) with complexity[j] < complexity[i] (i.e., lower complexity).

        A valid permutation is an ordering of [0, 1, ..., n-1] such that, for
        each computer i appearing after 0 in the order:
            - There exists a j before i in the order where j < i and complexity[j] < complexity[i].

        Returns the number of such permutations modulo 10^9 + 7.

        Args:
            complexity (List[int]): List of password complexities for each computer.

        Returns:
            int: Number of valid unlock order permutations modulo 10^9 + 7.

        Example:
            Input: complexity = [2, 4, 7]
            Output: 2
            Explanation:
                Valid permutations:
                - [0, 1, 2]
                - [0, 2, 1]
                Total = 2

        Time Complexity: O(N), where N is the number of computers (due to a single pass for verification).
        Space Complexity: O(1).

        LeetCode: Beats 95.00% of submissions
        """
        MOD = 10**9 + 7
        min_complexity = complexity[0]
        permutations = 1
        curr_fact = 1

        for i in range(1, len(complexity)):
            if complexity[i] <= min_complexity:
                return 0

            permutations = (permutations * curr_fact) % MOD
            curr_fact += 1

        return permutations
