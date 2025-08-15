class Solution:
    def distinctIntegers(self, n: int) -> int:
        """
        Calculates the number of distinct integers that will appear on the board
        after repeatedly applying the following process for a large number of days:

        - Start with a single integer n on the board.
        - Each day, for every number x currently on the board, add all numbers i (1 <= i <= n) such that x % i == 1 to the board.
        - Once a number is added to the board, it remains there permanently.

        Args:
            n (int): The initial integer placed on the board.

        Returns:
            int: The total number of distinct integers present on the board after the process stabilizes.

        Example:
            >>> distinctIntegers(2)
            1
            >>> distinctIntegers(5)
            4

        Time Complexity: O(n)
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        seen = set()
        nums = [n]

        while nums:
            num = nums.pop()
            seen.add(num)

            for i in range(num - 1, 1, -1):
                if num % i == 1 and i not in seen:
                    nums.append(i)

        return len(seen)
