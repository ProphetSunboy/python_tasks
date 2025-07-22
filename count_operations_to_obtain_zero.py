class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        """Counts the number of operations to make either num1 or num2 equal to zero.
        In each operation, subtract the smaller number from the larger one:
            - If num1 >= num2, set num1 = num1 - num2.
            - Otherwise, set num2 = num2 - num1.
        Repeat until either num1 == 0 or num2 == 0.

        Args:
            num1 (int): First non-negative integer.
            num2 (int): Second non-negative integer.

        Returns:
            int: The number of operations performed until one of the numbers becomes zero.

        Example:
            >>> countOperations(5, 4)
            5
            # Step 1: 5 - 4 = 1, so (1, 4)
            # Step 2: 4 - 1 = 3, so (1, 3)
            # Continue until one is zero.

        Time complexity: O(log(max(num1, num2))) in the worst case.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """

        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                n = max(num1 // num2, 1)
                num1 -= n * num2
                ops += n
            else:
                n = max(num2 // num1, 1)
                num2 -= n * num1
                ops += n

        return ops
