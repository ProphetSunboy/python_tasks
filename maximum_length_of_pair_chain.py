class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """
        You are given an array of n pairs pairs where pairs[i] = [lefti, righti]
        and lefti < righti.

        A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs
        can be formed in this fashion.

        Return the length longest chain which can be formed.

        You do not need to use up all the given intervals. You can select pairs
        in any order.


        :param list[list[int]] pairs: pairs where pairs[i] = [left, right]
        and left < right
        :returns int longest_chain: length of longest chain which can be formed

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 96.20%
        """
        sorted_pairs = sorted(pairs, key=lambda item: item[1])
        last = sorted_pairs[0][1]
        longest_chain = 1

        for i in range(len(sorted_pairs) - 1):
            if last < sorted_pairs[i + 1][0]:
                longest_chain += 1
                last = sorted_pairs[i + 1][1]

        return longest_chain
