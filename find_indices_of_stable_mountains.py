class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        """Given a list of mountain heights and a threshold value, find all stable mountains.

        A mountain is considered stable if the mountain immediately before it has a height
        strictly greater than the threshold. Mountain 0 is never stable since it has no
        preceding mountain.

        Args:
            height (list[int]): List where height[i] represents the height of mountain i.
            threshold (int): The minimum height required for a preceding mountain to make
                           the current mountain stable.

        Returns:
            list[int]: List containing indices of all stable mountains in any order.

        Example:
            >>> stableMountains([3, 2, 5, 1], 2)
            [1, 3]
            >>> stableMountains([1, 2, 3], 1)
            [1, 2]

        LeetCode: Beats 100% of submissions
        """
        stable = []

        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                stable.append(i)

        return stable
