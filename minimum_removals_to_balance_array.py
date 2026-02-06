class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        """
        Given an integer list nums and an integer k.

        A list is considered balanced if the value of its maximum element is at most
        k times the minimum element.

        You may remove any number of elements from nums without making it empty.

        Returns the minimum number of elements to remove so that the remaining
        list is balanced.

        Args:
            nums (List[int]): The input list.
            k (int): The balancing factor.

        Returns:
            int: The minimum number of elements to remove to balance the list.

        Example:
            Input: nums = [1, 3, 6, 19], k = 3
            Output: 2

        Time Complexity: O(n log n), where n is the length of nums due to sorting.
        Space Complexity: O(1), as only constant extra space is used.

        LeetCode: Beats 92.78% of submissions
        """
        nums.sort()
        n = len(nums)
        max_balanced_len = 0
        left = 0

        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1

            current_len = right - left + 1
            if current_len > max_balanced_len:
                max_balanced_len = current_len

        return n - max_balanced_len
