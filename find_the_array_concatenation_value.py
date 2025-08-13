class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        """
        Calculates the concatenation value of a list of integers.

        The concatenation value is computed by repeatedly concatenating the first and last elements of the list
        (as strings), converting the result back to an integer, and adding it to a running total. After each operation,
        the first and last elements are removed from the list. If only one element remains, its value is added to the total.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The concatenation value of the list.

        Example:
            >>> findTheArrayConcVal([7, 52, 2, 4])
            596
            # Explanation: 7 and 4 -> 74, 52 and 2 -> 522, total = 74 + 522 = 596

        Time Complexity: O(N), where N is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i, j = 0, len(nums) - 1
        conc_val = 0

        while i < j:
            conc_val += int(str(nums[i]) + str(nums[j]))

            i += 1
            j -= 1

        if i == j:
            conc_val += nums[i]

        return conc_val
