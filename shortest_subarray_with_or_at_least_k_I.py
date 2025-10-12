class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        Finds the length of the shortest non-empty sublist of nums whose bitwise OR is at least k.

        A sublist is considered "special" if the bitwise OR of all its elements is at least k.
        Returns the length of the shortest such sublist, or -1 if none exists.

        Args:
            nums (List[int]): List of non-negative integers.
            k (int): Target minimum bitwise OR value.

        Returns:
            int: Length of the shortest special sublist, or -1 if not found.

        Example:
            >>> minimumSubarrayLength([2, 8, 2, 6, 12], 8)
            1

        Time Complexity: O(n^2), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        shortest = 10**3

        for i in range(len(nums)):
            curr = nums[i]
            curr_len = 1
            if curr >= k:
                return curr_len

            for j in range(i + 1, len(nums)):
                curr |= nums[j]
                curr_len += 1

                if curr >= k and curr_len < shortest:
                    shortest = curr_len

        return shortest if shortest < 10**3 else -1
