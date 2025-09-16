class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Calculates the sum of XOR totals for every subset of the input list nums.

        The XOR total of a subset is defined as the bitwise XOR of all its elements (0 if the subset is empty).
        For example, the XOR total of [2, 5, 6] is 2 ^ 5 ^ 6 = 1.

        This function considers all possible subsets of nums (including the empty
        subset and subsets with repeated elements in different positions) and returns
        the sum of their XOR totals.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The sum of XOR totals for all subsets of nums.

        Example:
            >>> subsetXORSum([1, 3])
            6
            # Subsets: [], [1], [3], [1,3]
            # XORs:    0   1     3     1^3=2; sum = 0+1+3+2 = 6

        Time Complexity: O(n * 2^n), where n is the length of nums.
        Space Complexity: O(2^n), due to storage of intermediate XORs.

        LeetCode: Beats 100% of submissions
        """
        xors = []
        xor_total = 0

        for num in nums:
            curr = []
            for xor in xors:
                curr_xor = num ^ xor
                xor_total += curr_xor
                curr.append(curr_xor)

            xors += curr
            xor_total += num
            xors.append(num)

        return xor_total
