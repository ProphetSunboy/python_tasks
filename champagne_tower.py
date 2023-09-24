class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        After pouring some non-negative integer cups of champagne, return
        how full the jth glass in the ith row is (both i and j are 0-indexed.)

        We stack glasses in a pyramid, where the first row has 1 glass, the
        second row has 2 glasses, and so on until the 100th row.  Each glass
        holds one cup of champagne.

        Then, some champagne is poured into the first glass at the top.  When
        the topmost glass is full, any excess liquid poured will fall equally to
        the glass immediately to the left and right of it.  When those glasses
        become full, any excess champagne will fall equally to the left and
        right of those glasses, and so on.  (A glass at the bottom row has its
        excess champagne fall on the floor.)

        For example, after one cup of champagne is poured, the top most glass
        is full.  After two cups of champagne are poured, the two glasses on the
        second row are half full.  After three cups of champagne are poured,
        those two cups become full - there are 3 full glasses total now.  After
        four cups of champagne are poured, the third row has the middle glass
        half full, and the two outside glasses are a quarter full.

        :param int poured: number of poured champagne cups
        :param int query_row: ith row of champagne tower
        :param int query_glass: jth glass of champagne tower
        :returns float fullness: how full the jth glass in the ith row

        Time complexity: O(m*n)
        Space complexity: O(m*n)

        LeetCode: Beats 93.38%
        """
        glasses = []

        for i in range(1, query_row + 3):
            glasses.append([0] * i)

        glasses[0][0] = poured

        for i in range(query_row + 1):
            for j in range(len(glasses[i])):
                if glasses[i][j] > 1:
                    remainder = glasses[i][j] - 1
                    glasses[i][j] -= remainder

                    glasses[i + 1][j] += remainder / 2
                    glasses[i + 1][j + 1] += remainder / 2

        return glasses[query_row][query_glass]
