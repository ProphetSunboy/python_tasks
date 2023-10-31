class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        """
        You are given an integer list pref of size n. Find and return the list
        arr of size n that satisfies:

            pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

        Note that ^ denotes the bitwise-xor operation.

        It can be proven that the answer is unique.

        :param list[int] pref: integer list
        :returns list[int] arr: integer list

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 91.35%
        """
        arr = [pref[0]] * len(pref)

        for i in range(len(pref) - 1):
            arr[i + 1] = pref[i] ^ pref[i + 1]

        return arr
