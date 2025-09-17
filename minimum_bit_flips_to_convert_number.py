class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Calculates the minimum number of bit flips required to convert the integer 'start' to 'goal'.

        A bit flip is defined as toggling a single bit in the binary representation of a number
        (from 0 to 1 or from 1 to 0). Leading zeros are considered in the comparison.

        Args:
            start (int): The starting integer.
            goal (int): The target integer.

        Returns:
            int: The minimum number of bit flips needed to convert 'start' to 'goal'.

        Example:
            >>> minBitFlips(10, 7)
            3

        Time Complexity: O(k), where k is the number of bits in the larger of 'start' or 'goal'.
        Space Complexity: O(k)

        LeetCode: Beats 100% of submissions
        """
        start_b = bin(start)[2:]
        goal_b = bin(goal)[2:]

        if len(goal_b) >= len(start_b):
            start_b = start_b.zfill(len(goal_b))
        else:
            goal_b = goal_b.zfill(len(start_b))

        bit_flips = 0
        for i in range(len(goal_b)):
            if goal_b[i] != start_b[i]:
                bit_flips += 1

        return bit_flips
