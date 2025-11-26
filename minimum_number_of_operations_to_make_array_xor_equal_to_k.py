class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Given a 0-indexed integer list nums and a positive integer k, return the
        minimum number of bit flips required to make the bitwise XOR of all
        elements in nums equal to k.

        You may perform the following operation any number of times:
            choose any element in the list and flip any bit in its binary
            representation (i.e., change a 0 to 1 or 1 to 0).

        You can also flip leading zero bits.

        Args:
            nums (List[int]): A list of integers to operate on.
            k (int): Target value for the final XOR of the list.

        Returns:
            int: Minimum number of bit-flip operations required to make the XOR
            of all elements equal to k.

        Example:
            Input: nums = [2, 1, 3], k = 7
            Output: 3

        Time Complexity: O(N + L), where N is the length of nums and L is the bit length of the maximum number and k.
        Space Complexity: O(1)

        LeetCode: Beats 94.47% of submissions
        """
        list_xor = nums[0]

        for i in range(1, len(nums)):
            list_xor ^= nums[i]

        bin_list_xor = bin(list_xor)[2:]
        bin_k = bin(k)[2:]
        if list_xor > k:
            bin_k = bin_k.zfill(len(bin_list_xor))
        else:
            bin_list_xor = bin_list_xor.zfill(len(bin_k))

        return sum([bin_list_xor[i] != bin_k[i] for i in range(len(bin_k))])
