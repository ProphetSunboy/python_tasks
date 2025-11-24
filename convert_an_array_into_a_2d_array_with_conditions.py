class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer list nums, construct a 2D lisr according to the
        following rules:

        - Each row contains only distinct integers (no duplicates in any row).
        - The resulting 2D list contains all elements from nums.
        - The number of rows is minimized.
        - The 2D list may have a variable number of columns per row.
        - If multiple valid answers exist, return any of them.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[List[int]]: The constructed 2D list with minimal number of
            rows satisfying the above conditions.

        Example:
            Input: nums = [1,3,4,1,2,3,1]
            Output: [
                        [1,3,4,2],
                        [1,3],
                        [1]
                    ]
            (Each row contains distinct elements, and the number of rows is minimized.)

        Time Complexity: O(n), where n is the number of elements in nums.
        Space Complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)
        res = []

        changes = 1
        while changes:
            curr_row = []
            changes = 0
            for num, val in c.items():
                if val > 0:
                    curr_row.append(num)
                    c[num] -= 1
                    changes += 1

            if changes > 0:
                res.append(curr_row)

        return res
