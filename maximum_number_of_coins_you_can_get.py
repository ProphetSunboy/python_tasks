class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        Given 3n piles of coins (represented by the list `piles`), you, Alice,
        and Bob take turns picking coins in rounds:
            - In each round, select any 3 remaining piles.
            - Alice picks the pile with the most coins.
            - You pick the next largest pile.
            - Bob picks the smallest pile.
        Repeat until there are no piles left.

        The function returns the maximum total number of coins *you* can collect
        following this strategy.

        Args:
            piles (List[int]): List of integers where piles[i] is the number of
            coins in the ith pile. The length of piles is a multiple of 3.

        Returns:
            int: The maximum number of coins you can obtain.

        Example:
            Input: piles = [2,4,1,2,7,8]
            Output: 9
            Explanation: Sort and pick groups: [1,2,2,4,7,8].
            In two rounds, you pick 7 and 2.

        Time Complexity: O(N log N), for sorting, where N is the size of piles.
        Space Complexity: O(1), ignoring the space for sorting output.

        LeetCode: Beats 92.57% of submissions
        """
        piles.sort()
        coins = 0

        i, j = len(piles) - 2, 0
        while j < i:
            coins += piles[i]
            i -= 2
            j += 1

        return coins
