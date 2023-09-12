class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Given a string s, return the minimum number of characters you need to
        delete to make s good.

        A string s is called good if there are no two different characters in s
        that have the same frequency.

        :param str s: original string
        :returns int deletions: minimum number of characters you need to delete
        to make s good

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 92.31%
        """
        count = sorted(collections.Counter(s).values(), reverse=True)
        seen = []
        deletions = 0

        for val in count:
            if val in seen:
                num = val - seen[-1] + 1
                deletions += num

                if seen[-1] > 1:
                    seen.append(seen[-1] - 1)
            else:
                seen.append(val)

        return deletions
