class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        """
        Finds the largest 'almost missing' integer in the given list.

        An integer x is considered 'almost missing' from nums if it appears in exactly one sublist of size k within nums.
        A sublist is a contiguous sequence of elements within the list.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The size of the sublist to consider.

        Returns:
            int: The largest integer that is 'almost missing' from nums, or -1 if no such integer exists.

        Example:
            >>> largestInteger([3, 9, 2, 1, 7], 3)
            7

        Time Complexity: O(n * k), where n is the length of nums.
        Space Complexity: O(u), where u is the number of unique elements in nums.

        LeetCode: Beats 100% of submissions
        """
        freq = {}

        for i in range(len(nums) - k + 1):
            for j in set(nums[i : i + k]):
                freq[j] = freq.get(j, 0) + 1

        largest = -1
        for num, f in freq.items():
            if f == 1 and num > largest:
                largest = num

        return largest
