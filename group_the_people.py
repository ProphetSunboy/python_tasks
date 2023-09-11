class FastSolution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        """
        There are n people that are split into some unknown number of groups.
        Each person is labeled with a unique ID from 0 to n - 1.

        You are given an integer array groupSizes, where groupSizes[i] is the
        size of the group that person i is in. For example, if
        groupSizes[1] = 3, then person 1 must be in a group of size 3.

        Return a list of groups such that each person i is in a group of size
        groupSizes[i].

        Each person should appear in exactly one group, and every person must be
        in a group. If there are multiple answers, return any of them. It is
        guaranteed that there will be at least one valid solution for the given
        input.

        :param list[int] groupsSizes: sizes of the groups that persons is in
        :returns list[list[int]] groups: list of groups such that each person i
        is in a group of size groupSizes[i]

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 97.99%
        """
        groups = []
        g = {}

        for i, size in enumerate(groupSizes):
            g[size] = g.get(size, []) + [i]

        for key, val in g.items():
            for i in range(0, len(val), key):
                groups.append(val[i : i + key])

        return groups


class SlowSolution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = []

        for i in range(len(groupSizes)):
            group_find = False
            for group in groups:
                if group_find:
                    break

                if len(group) == groupSizes[i]:
                    for j in range(len(group)):
                        if group[j] == -1:
                            group[j] = i
                            group_find = True
                            break

            if not group_find:
                groups.append([-1] * groupSizes[i])
                groups[-1][0] = i

        return groups
