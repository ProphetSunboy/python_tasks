class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """
        Given a 0-indexed integer list nums and an integer value, returns the maximum possible MEX (minimum excluded non-negative integer)
        that can be obtained by adding or subtracting value any number of times to any element in nums.

        The MEX of a list is the smallest non-negative integer not present in the list.

        Operation: For any index i, you may perform nums[i] += value or nums[i] -= value any number of times (including zero).

        Args:
            nums (List[int]): List of integers to operate on.
            value (int): The value to add or subtract from elements.

        Returns:
            int: The largest possible MEX obtainable after performing any number of allowed operations.

        Example:
            >>> findSmallestInteger([1, 2, 3], 2)
            2
            >>> findSmallestInteger([0, 1, 2], 1)
            3

        Time Complexity: O(n), where n is the length of nums (for iterating over nums).
        Space Complexity: O(value) (for the remainder counts).
        """
        count = Counter()

        for num in nums:
            count[num % value] += 1

        i = 0
        while True:
            r = i % value
            if count[r] > 0:
                count[r] -= 1
                i += 1
            else:
                return i
