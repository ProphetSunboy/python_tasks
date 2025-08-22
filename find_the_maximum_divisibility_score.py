class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        """
        Given two integer lists, nums and divisors, compute the divisibility score for each element in divisors.

        The divisibility score of divisors[i] is defined as the number of elements in nums that are divisible by divisors[i].

        Returns the integer divisors[i] with the highest divisibility score.
        If multiple divisors have the same maximum score, returns the smallest such divisor.

        Args:
            nums (list[int]): List of integers to be checked for divisibility.
            divisors (list[int]): List of divisors to compute scores for.

        Returns:
            int: The divisor with the maximum divisibility score (smallest in case of tie).

        Example:
            >>> maxDivScore([4, 7, 9, 3, 9], [5, 2, 3])
            3

        Time Complexity: O(m * n), where m = len(nums), n = len(divisors)
        Space Complexity: O(n)

        LeetCode: Beats 91.08% of submissions
        """
        divisors.sort()
        div_score = [0] * len(divisors)

        for num in nums:
            for i, div in enumerate(divisors):
                if div > num // 2:
                    break
                if num % div == 0:
                    div_score[i] += 1

        for i, div in enumerate(divisors):
            if div in nums:
                div_score[i] += 1

        max_score = max(div_score)

        for i, score in enumerate(div_score):
            if score == max_score:
                return divisors[i]
