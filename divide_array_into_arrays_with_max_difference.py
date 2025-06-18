class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """Divide a list into sublists of size 3 with maximum difference constraint.

        Given an integer list nums of size n (where n is a multiple of 3) and a positive
        integer k, divide the list into n/3 sublists of size 3 such that the difference
        between any two elements in each sublist is less than or equal to k.

        Args:
            nums (list[int]): List of integers to divide (length must be multiple of 3)
            k (int): Maximum allowed difference between any two elements in a sublist

        Returns:
            list[list[int]]: 2D list containing the divided sublists, or empty list
                           if division is impossible

        Examples:
            >>> divideArray([1,3,4,8,9,9], 3)
            [[1,3,4], [8,9,9]]  # Valid division with max difference ≤ 3
            >>> divideArray([1,3,4,8,9,9], 1)
            []  # Impossible to divide with max difference ≤ 1

        Time complexity: O(n log n) - dominated by sorting
        Space complexity: O(n) - to store sorted array and result

        LeetCode: Beats 90.30% of submissions
        """
        ans = []
        s_nums = sorted(nums)

        for i in range(0, len(s_nums), 3):
            if s_nums[i + 2] - s_nums[i] <= k:
                ans.append([s_nums[i], s_nums[i + 1], s_nums[i + 2]])
            else:
                ans = []
                break

        return ans
