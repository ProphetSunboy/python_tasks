class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        """
        Given two integer lists, fruits and baskets, each of length n:
            - fruits[i] is the quantity of the ith type of fruit.
            - baskets[j] is the capacity of the jth basket.

        For each fruit type (from left to right), place it in the leftmost available
        basket with capacity >= that fruit's quantity.
        Each basket can hold only one type of fruit.
        If a fruit type cannot be placed in any basket, it remains unplaced.

        Returns the number of fruit types that remain unplaced after all possible allocations.

        Args:
            fruits (list[int]): Quantities of each fruit type.
            baskets (list[int]): Capacities of each basket.

        Returns:
            int: Number of unplaced fruit types.

        Example:
            >>> numOfUnplacedFruits([2, 3, 5], [3, 2, 5])
            1
            >>> numOfUnplacedFruits([4, 2, 7], [3, 2, 5])
            1

        Time complexity: O(n^2), where n is the length of the lists.
        Space complexity: O(1).

        LeetCode: Beats 90.04% of submissions
        """
        unplaced = 0

        for fruit in fruits:
            is_unplaced = True
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    is_unplaced = False
                    baskets[i] = 0
                    break

            unplaced += is_unplaced

        return unplaced
