class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        """
        Constructs a transformed list based on circular movement rules.

        For each index `i` in the input integer list `nums` (treated as circular):
            - If nums[i] > 0: Move nums[i] steps to the right (wrapping around if necessary) and set result[i] to the value at the resulting index.
            - If nums[i] < 0: Move abs(nums[i]) steps to the left (wrapping around if necessary) and set result[i] to the value at the resulting index.
            - If nums[i] == 0: Set result[i] to nums[i].

        Args:
            nums (List[int]): The circular integer list to transform.

        Returns:
            List[int]: The transformed list following the above rules.

        Example:
            >>> constructTransformedArray([2, -1, 0, 3])
            [0, 2, 0, 0]

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n) for the result list.

        LeetCode: Beats 95.52% of submissions
        """
        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                res[i] = nums[(i + nums[i]) % len(nums)]
            elif nums[i] < 0:
                res[i] = nums[(i - abs(nums[i])) % len(nums)]
            else:
                res[i] = nums[i]

        return res
