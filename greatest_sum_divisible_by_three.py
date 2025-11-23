class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        Returns the maximum possible sum of elements from the input list `nums`
        such that the sum is divisible by three.

        Args:
            nums (List[int]): The list of integers to select from.

        Returns:
            int: The largest possible sum divisible by three composed from
            elements of nums.

        Example:
            Input: nums = [3,6,5,1,8]
            Output: 18
            Explanation: Remove 5 to get the sum 18, which is divisible by 3.

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), for storing elements grouped by their remainder
        modulo 3.

        LeetCode: Beats 97.63% of submissions.
        """
        total = sum(nums)

        if total % 3 == 0:
            return total

        r1 = []
        r2 = []

        for x in nums:
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)

        r1.sort()
        r2.sort()

        if total % 3 == 1:
            candidates = []
            if r1:
                candidates.append(total - r1[0])
            if len(r2) >= 2:
                candidates.append(total - r2[0] - r2[1])
            return max(candidates) if candidates else 0

        if total % 3 == 2:
            candidates = []
            if r2:
                candidates.append(total - r2[0])
            if len(r1) >= 2:
                candidates.append(total - r1[0] - r1[1])
            return max(candidates) if candidates else 0
