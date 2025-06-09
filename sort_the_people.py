class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        """Sorts a list of names based on their corresponding heights in descending order.

        Given two lists of equal length where names[i] corresponds to heights[i], returns
        the names list sorted by heights in descending order.

        Args:
            names (list[str]): List of person names
            heights (list[int]): List of corresponding heights (distinct positive integers)

        Returns:
            list[str]: Names sorted by heights in descending order

        Example:
            >>> sortPeople(["Mary","John","Emma"], [180,165,170])
            ['Mary', 'Emma', 'John']

        Time complexity: O(n log n) - due to sorting operation
        Space complexity: O(n) - for storing the sorted result

        LeetCode: Beats 100% of submissions
        """
        return [
            name
            for name, height in sorted(
                zip(names, heights), key=lambda x: x[1], reverse=True
            )
        ]
