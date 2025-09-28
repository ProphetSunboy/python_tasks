class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        Given n chips, where the position of the ith chip is position[i], you can move chips as follows:
            - Move by 2 units (position[i] + 2 or position[i] - 2) at zero cost.
            - Move by 1 unit (position[i] + 1 or position[i] - 1) at a cost of 1.

        The goal is to move all chips to the same position with the minimum total cost.

        Args:
            position (List[int]): List of integers representing the positions of the chips.

        Returns:
            int: The minimum cost required to move all chips to the same position.

        Example:
            >>> minCostToMoveChips([1,2,3])
            1
            >>> minCostToMoveChips([2,2,2,3,3])
            2

        Time Complexity: O(n), where n is the number of chips.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        odd = 0
        even = 0

        for p in position:
            if p % 2:
                odd += 1
            else:
                even += 1

        return min(odd, even)
