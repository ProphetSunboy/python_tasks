class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        """Finds the most frequent even element in the given list of integers.
        If there are multiple such elements, returns the smallest one.
        If there is no even element, returns -1.

        Args:
            nums (list[int]): List of integers.

        Returns:
            int: The most frequent even element, or the smallest one in case of a tie.
                 Returns -1 if no even element exists.

        Example:
            >>> mostFrequentEven([0,1,2,2,4,4,1])
            2

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(m), where m is the number of unique even numbers.

        LeetCode: Beats 99.79% of submissions
        """
        evens = dict()

        for num in nums:
            if num % 2 == 0:
                evens[num] = evens.get(num, 0) + 1

        smallest = -1
        max_freq = 0
        for even, freq in evens.items():
            if freq > max_freq:
                smallest = even
                max_freq = freq
            elif freq == max_freq:
                if even < smallest:
                    smallest = even

        return smallest
