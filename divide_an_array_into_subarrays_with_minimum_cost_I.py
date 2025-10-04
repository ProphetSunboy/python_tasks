class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        """
        Given a list of integers nums of length n, divide nums into 3 disjoint contiguous sublists.

        The cost of a sublist is the value of its first element. The total cost is the sum of the costs of the three sublists.

        Return the minimum possible total cost of such a division.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum possible sum of the costs of the three contiguous sublists.

        Example:
            >>> minimumCost([1,2,3,4,5])
            6

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        min_cost = nums[0]
        nums.sort()

        if min_cost == nums[0]:
            min_cost += nums[1] + nums[2]
        elif min_cost == nums[1]:
            min_cost += nums[0] + nums[2]
        else:
            min_cost += nums[0] + nums[1]

        return min_cost
