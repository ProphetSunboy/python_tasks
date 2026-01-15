class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        """
        Given two integers, n and m, and two integer lists, hBars and vBars,
        representing the indices of removable horizontal and vertical bars
        in a grid of (n + 2) horizontal and (m + 2) vertical bars that create
        1 x 1 unit cells.

        Bars are indexed starting from 1.
        Some bars can be removed from the grid as specified by hBars and vBars;
        other bars are fixed.

        Returns the maximum possible area of a square-shaped hole that can be
        created in the grid after removing some bars (possibly none).

        Args:
            n (int): Number of horizontal bars (excluding the two boundary bars).
            m (int): Number of vertical bars (excluding the two boundary bars).
            hBars (List[int]): Indices of removable horizontal bars.
            vBars (List[int]): Indices of removable vertical bars.

        Returns:
            int: Maximum area of a square hole in the grid.

        Example:
            Input: n = 2, m = 1, hBars = [2, 3], vBars = [2]
            Output: 4  # Possible to create a 2x2 square hole

        Time Complexity: O(H log H + V log V), where H = len(hBars) and V = len(vBars)
        Space Complexity: O(1), aside from the input and output.

        LeetCode: Beats 100% of submissions
        """
        hBars.sort()
        vBars.sort()

        h_counter = 0
        curr = 1
        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i - 1] == 1:
                curr += 1
            else:
                if curr > h_counter:
                    h_counter = curr

                curr = 1

        if curr > h_counter:
            h_counter = curr

        v_counter = 0
        curr = 1
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i - 1] == 1:
                curr += 1
            else:
                if curr > v_counter:
                    v_counter = curr

                curr = 1

        if curr > v_counter:
            v_counter = curr

        side = min(h_counter, v_counter) + 1

        return side**2
