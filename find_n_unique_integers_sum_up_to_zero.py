class Solution:
    def sumZero(self, n: int) -> list[int]:
        """
        Returns a list of n unique integers that sum up to 0.

        Given an integer n, constructs any list of n distinct integers such that their sum is zero.

        Args:
            n (int): The number of unique integers to generate.

        Returns:
            List[int]: A list of n unique integers whose sum is 0.

        Example:
            >>> sumZero(5)
            [1, 2, 3, 4, -10]
            # (or any permutation of 4 unique numbers and their negative sum)

        Time Complexity: O(n), where n is the input integer.
        Space Complexity: O(n) (for the output list).

        LeetCode: Beats 100% of submissions
        """
        nums = []
        s_nums = 0

        for i in range(1, n):
            nums.append(i)
            s_nums += i

        nums.append(-s_nums)

        return nums
