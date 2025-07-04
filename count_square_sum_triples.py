class Solution:
    def countTriples(self, n: int) -> int:
        """Counts the number of square sum triples (a, b, c) such that:
            - 1 <= a, b, c <= n
            - a^2 + b^2 = c^2

        Args:
            n (int): The upper bound for a, b, and c.

        Returns:
            int: The number of valid square sum triples.

        Example:
            >>> countTriples(5)
            2

        # Time complexity: O(n^2)
        # Space complexity: O(1)
        """
        counter = 0

        for i in range(1, n):
            for j in range(i + 1, n):
                k = math.sqrt((i**2 + j**2))

                if int(k) == k and k <= n:
                    counter += 2

        return counter
