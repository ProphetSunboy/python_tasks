# First attempt
class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)

        flag = True
        while flag:
            change = False
            for i in range(len(candies)):
                if (
                    ratings[i] > ratings[min(i + 1, len(ratings) - 1)]
                    and ratings[i] > ratings[max(i - 1, 0)]
                ):
                    if (
                        candies[i] <= candies[max(i - 1, 0)]
                        or candies[i] <= candies[min(i + 1, len(candies) - 1)]
                    ):
                        candies[i] = (
                            max(
                                candies[max(i - 1, 0)],
                                candies[min(i + 1, len(candies) - 1)],
                                candies[i],
                            )
                            + 1
                        )
                        change = True
                elif ratings[i] > ratings[max(i - 1, 0)]:
                    if candies[i] <= candies[max(i - 1, 0)]:
                        candies[i] = candies[max(i - 1, 0)] + 1
                        change = True
                elif ratings[i] > ratings[min(i + 1, len(ratings) - 1)]:
                    if candies[i] <= candies[min(i + 1, len(candies) - 1)]:
                        candies[i] = candies[min(i + 1, len(candies) - 1)] + 1
                        change = True

            if not change:
                flag = False

        return sum(candies)


# Second attempt
class Solution(object):
    def candy(self, ratings: list[int]) -> int:
        """Distribute candies to children based on their ratings.

        There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
        You are giving candies to these children subjected to the following requirements:
        1. Each child must have at least one candy.
        2. Children with a higher rating get more candies than their neighbors.

        Args:
            ratings (list[int]): list of integer ratings for each child

        Returns:
            int: The minimum total number of candies needed to satisfy the requirements

        Example:
            >>> candy([1,0,2])
            5
            >>> candy([1,2,2])
            4

        Time complexity: O(n) where n is the number of children
        Space complexity: O(n) to store the candies list
        """
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
