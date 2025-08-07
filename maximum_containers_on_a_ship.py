class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        """
        Given an n x n cargo deck and a container weight w, determine the maximum number of containers
        that can be loaded onto the ship without exceeding the ship's maximum weight capacity, maxWeight.

        Each cell on the deck can hold one container of weight w. The total number of containers cannot
        exceed n * n, and the total weight of all loaded containers must not exceed maxWeight.

        Args:
            n (int): The size of the cargo deck (n x n).
            w (int): The weight of each container.
            maxWeight (int): The ship's maximum weight capacity.

        Returns:
            int: The maximum number of containers that can be loaded onto the ship.

        Examples:
            >>> maxContainers(3, 2, 15)
            7
            >>> maxContainers(2, 5, 100)
            4

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        max_containers = maxWeight // w
        if max_containers < n * n:
            return max_containers

        return n * n
