class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Returns the number of ways to distribute n candies among 3 children such that no child receives more than 'limit' candies.

        Args:
            n (int): Total number of candies to distribute.
            limit (int): Maximum candies any child can receive.

        Returns:
            int: The total number of valid distributions.

        Example:
            >>> distributeCandies(5, 2)
            3

        Time Complexity: O(limit^2)
        Space Complexity: O(1)
        """
        total = 0

        for i in range(limit + 1):
            for j in range(limit + 1):
                if i + j > n:
                    break
                elif n - (i + j) <= limit:
                    total += 1

        return total
