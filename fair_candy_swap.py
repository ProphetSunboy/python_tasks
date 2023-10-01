class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        """
        Alice and Bob have a different total number of candies. You are given
        two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the
        number of candies of the ith box of candy that Alice has and bobSizes[j]
        is the number of candies of the jth box of candy that Bob has.

        Since they are friends, they would like to exchange one candy box each
        so that after the exchange, they both have the same total amount of
        candy. The total amount of candy a person has is the sum of the number
        of candies in each box they have.

        Return an integer array answer where answer[0] is the number of candies
        in the box that Alice must exchange, and answer[1] is the number of
        candies in the box that Bob must exchange. If there are multiple
        answers, you may return any one of them. It is guaranteed that at least
        one answer exists.

        :param list[int] aliceSizes: boxes of candies
        :param list[int] bobSizes: boxes of candies
        :returns list[int] answer: boxes to exchange

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.09%
        """
        alice = sum(aliceSizes)
        bob_s = sum(bobSizes)
        bob_set = set(bobSizes)

        for el in aliceSizes:
            val = (bob_s - alice) / 2 + el

            if val in bob_set:
                return [el, val]
