class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        """
        Given two lists:
            - apple: a list of integers where apple[i] is the number of apples in the i-th pack.
            - capacity: a list of integers where capacity[j] is the capacity of the j-th box.

        The goal is to find the minimum number of boxes needed to redistribute all apples from the packs into the boxes.
        Apples from the same pack can be split among different boxes.

        Args:
            apple (list[int]): Number of apples in each pack.
            capacity (list[int]): Capacity of each box.

        Returns:
            int: The minimum number of boxes required to hold all apples.

        Example:
            >>> minimumBoxes([1, 3, 2], [4, 3, 1])
            2

        Time complexity: O(m log m), where m is the length of capacity (due to sorting).
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        apples = sum(apple)
        capacity.sort(reverse=True)
        i = 0

        while apples > 0:
            apples -= capacity[i]
            i += 1

        return i
