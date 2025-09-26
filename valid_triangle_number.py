class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Counts the number of valid triplets in the list that can form the sides of a triangle.

        A triplet (i, j, k) forms a valid triangle if:
            nums[i] + nums[j] > nums[k], where i < j < k.

        Args:
            nums (List[int]): List of non-negative integers representing side lengths.

        Returns:
            int: The number of valid triplets that can form a triangle.

        Example:
            >>> triangleNumber([2, 2, 3, 4])
            3
            # Explanation: The valid triplets are (2,3,4), (2,3,4), and (2,2,3).

        Time Complexity: O(N^2), where N is the length of nums.
        Space Complexity: O(1) (ignoring the space used by sorting).

        LeetCode: Beats 100% of submissions
        """
        nums.sort()
        valid = 0
        n = len(nums)

        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    valid += j - i
                    j -= 1
                else:
                    i += 1

        return valid
