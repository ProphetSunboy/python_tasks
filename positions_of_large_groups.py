class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        """
        Given a string s of lowercase English letters, return the intervals of
        every large group sorted in increasing order.

        In a string s of lowercase letters, these letters form consecutive
        groups of the same character.

        For example, a string like s = "abbxxxxzyy" has the groups "a", "bb",
        "xxxx", "z", and "yy".

        A group is identified by an interval [start, end], where start and end
        denote the start and end indices (inclusive) of the group. In the above
        example, "xxxx" has the interval [3,6].

        A group is considered large if it has 3 or more characters.

        Return the intervals of every large group sorted in increasing order by
        start index.

        :param str s: string of lowercase English letters
        :returns list[list[int]] intervals: every large group sorted in increasing order

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 98.25%
        """
        groups = []

        start = 0
        curr = s[0]
        for i, ch in enumerate(s):
            if curr != ch:
                if i - 1 - start + 1 >= 3:
                    groups.append([start, i - 1])
                start = i
                curr = ch

        if i - start + 1 >= 3:
            groups.append([start, i])

        return sorted(groups)
