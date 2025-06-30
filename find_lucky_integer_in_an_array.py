class Solution:
    def findLucky(self, arr: list[int]) -> int:
        """Finds the largest lucky integer in a list.

        A lucky integer is an integer whose frequency in the list is equal to
        its value. This method returns the largest such integer. If no lucky
        integer is found, it returns -1.

        Args:
            arr (list[int]): The list of integers to search.

        Returns:
            int: The largest lucky integer, or -1 if none exists.

        Example:
            >>> findLucky([2, 2, 3, 4])
            2
            >>> findLucky([1, 2, 2, 3, 3, 3])
            3
            >>> findLucky([5])
            -1

        LeetCode: Beats 100% of submissions
        """
        c = Counter(arr)
        max_lucky = -1

        for num, freq in c.items():
            if num == freq:
                if num > max_lucky:
                    max_lucky = num

        return max_lucky
