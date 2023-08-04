class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        """
        Assume you are an awesome parent and want to give your children some
        cookies. But, you should give each child at most one cookie.

        Each child i has a greed factor g[i], which is the minimum size of a
        cookie that the child will be content with; and each cookie j has a
        size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
        and the child i will be content. Your goal is to maximize the number of
        your content children and output the maximum number.

        :param list[int] g: contains minimum sizes of a cookies that the children will be content with
        :param list[int] s: contains sizes of a cookies
        :returns int content: number of content children

        Time complexity: O(nlogn)
        Space complexity: O(1)

        LeetCode: Beats 99.37%
        """
        g.sort()
        s.sort()
        i, j = len(g) - 1, len(s) - 1
        content = 0

        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                content += 1
                j -= 1

            i -= 1

        return content
