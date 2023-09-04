class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        """
        Given an list of numbers arr, return True if the list can be
        rearranged to form an arithmetic progression. Otherwise, return False.

        A sequence of numbers is called an arithmetic progression if the
        difference between any two consecutive elements is the same.

        :param list[int] arr: list of integer numbers
        :returns bool res: possible to form an arithmetic progression

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 93.2%
        """
        asc = sorted(arr)

        diff_asc = asc[0] - asc[1]
        asc_flag = True

        for i in range(len(asc) - 1):
            if asc[i] - asc[i + 1] != diff_asc:
                asc_flag = False
                break

        if asc_flag:
            return True

        desc = sorted(arr, reverse=True)

        diff_desc = desc[0] - desc[1]
        desc_flag = True

        for i in range(len(desc) - 1):
            if desc[i] - desc[i + 1] != diff_desc:
                desc_flag = False
                break

        return desc_flag
