class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        """
        Counts the number of incremovable sublists in a given list.

        An incremovable sublist is a contiguous, non-empty sequence of the input
        list that, when removed, results in the remaining elements forming a
        strictly increasing sequence. The list is 0-indexed and consists of positive integers.

        An empty list is considered strictly increasing.

        Args:
            nums (List[int]): The input list of positive integers.

        Returns:
            int: The total number of incremovable sublists.

        Example:
            >>> incremovableSubarrayCount([1, 2, 3, 4])
            10

        Time Complexity: O(n^3), where n is the length of the input list, due to the brute-force approach.
        Space Complexity: O(n), for temporary lists created during computation.
        """
        n = len(nums)
        ans = 0

        def strictly_increasing(arr):
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

        for l in range(n):
            for r in range(l, n):
                new_arr = nums[:l] + nums[r + 1 :]
                if strictly_increasing(new_arr):
                    ans += 1
        return ans
