class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """Determines which kids can have the greatest number of candies after receiving extra candies.

        Given a list of integers `candies`, where `candies[i]` is the number of candies the i-th kid has,
        and an integer `extraCandies`, returns a list of booleans where the i-th value is True if, after
        giving all extraCandies to the i-th kid, they have the greatest (or equal greatest) number of candies
        among all kids.

        Args:
            candies (list[int]): List of the number of candies each kid has.
            extraCandies (int): Number of extra candies to give to a single kid.

        Returns:
            list[bool]: List indicating for each kid if they can have the greatest number of candies.

        Examples:
            >>> kidsWithCandies([2,3,5,1,3], 3)
            [True, True, True, False, True]
            >>> kidsWithCandies([4,2,1,1,2], 1)
            [True, False, False, False, False]


        Time complexity: O(N), where N is the number of kids.
        Space complexity: O(N), for the result list.

        LeetCode: Beats 100% of submissions
        """
        max_candies = max(candies)

        return [candie + extraCandies >= max_candies for candie in candies]
