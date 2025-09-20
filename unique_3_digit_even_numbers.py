class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        """
        Given a list of digits, count the number of distinct three-digit even numbers that can be formed.

        Rules:
            - Each digit from the input can be used at most once per number.
            - The number must not have a leading zero.
            - The number must be even (i.e., its last digit is even).

        Args:
            digits (List[int]): The list of digits to use.

        Returns:
            int: The count of unique three-digit even numbers that can be formed.

        Example:
            >>> totalNumbers([1, 2, 3, 4])
            12

        Time Complexity: O(n^3), where n is the number of digits.
        Space Complexity: O(1) (since the number of possible three-digit numbers is bounded).

        LeetCode: Beats 98.39% of submissions
        """
        unique = set()
        even = {i: digits[i] for i in range(len(digits)) if digits[i] % 2 == 0}

        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if j == i:
                    continue

                for k, n in even.items():
                    if k == i or k == j:
                        continue

                    unique.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        return len(unique)
