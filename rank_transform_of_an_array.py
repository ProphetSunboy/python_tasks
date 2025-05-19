class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """
        Given a list of integers arr, replace each element with its rank.

        The rank represents how large the element is. The rank has the following
        rules:

        Rank is an integer starting from 1.
        The larger the element, the larger the rank. If two elements are equal,
        their rank must be the same.
        Rank should be as small as possible.


        LeetCode Beats 97.59%
        """
        l = sorted(set(arr))
        ranking = dict()

        for i, num in enumerate(l, 1):
            ranking[num] = i

        rank = []
        for num in arr:
            rank.append(ranking[num])

        return rank
