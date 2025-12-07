class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        """
        Sorts a list of integers based on their binary reflection.

        The binary reflection of a positive integer is defined as the decimal
        value obtained by reversing the order of its binary digits
        (ignoring leading zeros in the original number).

        The list is sorted in ascending order based on the binary reflection of
        each element. If two numbers have the same binary reflection, the
        smaller original number comes first.

        Args:
            nums (List[int]): A list of positive integers.

        Returns:
            List[int]: The sorted list according to binary reflections.

        Example:
            Input: nums = [13, 7, 2]
            - 13 in binary: '1101' -> reversed: '1011' = 11 (decimal)
            - 7 in binary: '111' -> reversed: '111' = 7 (decimal)
            - 2 in binary: '10' -> reversed: '01' = 1 (decimal)
            Output: [2, 7, 13]  # ordered by [1, 7, 11]

        Time Complexity: O(N log N), where N is the number of elements in nums.
        Space Complexity: O(N), due to the sorting output.

        LeetCode: Beats 98.41% of submissions
        """
        return sorted(nums, key=lambda x: (int(bin(x)[2:][::-1], 2), x))
