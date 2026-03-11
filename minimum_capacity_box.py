class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        """
        Given an integer list capacity, where capacity[i] represents the
        capacity of the ith box, and an integer itemSize representing the size
        of an item, return the index of the box with the minimum capacity that
        can store the item.

        The ith box can store the item if capacity[i] >= itemSize.

        If multiple such boxes exist, return the smallest index.
        If no box can store the item, return -1.

        Args:
            capacity (List[int]): List of capacities for each box.
            itemSize (int): The size of the item to store.

        Returns:
            int: Index of the box with the minimum capacity that can store
                the item, or -1 if no such box exists.

        Example:
            Input: capacity = [1,5,3,7], itemSize = 3
            Output: 2

        Time Complexity: O(n), where n is the number of boxes.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        min_cap = float("inf")
        idx = -1

        for i, cap in enumerate(capacity):
            if cap >= itemSize and cap < min_cap:
                min_cap = cap
                idx = i

        return idx
