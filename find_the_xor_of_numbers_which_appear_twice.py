class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        """
        Given an integer list nums where each number appears either once or twice,
        return the bitwise XOR of all numbers that appear exactly twice in the list.
        If no number appears twice, return 0.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The XOR of all numbers appearing twice, or 0 if none.

        Example:
            >>> duplicateNumbersXOR([1, 2, 3, 2, 1, 4])
            3

        Time Complexity: O(n)
        Space Complexity: O(n) (due to counter)

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)
        xor = 0

        for num, freq in c.items():
            if freq == 2:
                xor ^= num

        return xor
