class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        In a town, there are n people labeled from 1 to n. There is a rumor that
        one of these people is secretly the town judge.

        If the town judge exists, then:

            The town judge trusts nobody.
            Everybody (except for the town judge) trusts the town judge.
            There is exactly one person that satisfies properties 1 and 2.

        You are given a list trust where trust[i] = [ai, bi] representing that
        the person labeled ai trusts the person labeled bi. If a trust
        relationship does not exist in trust array, then such a trust
        relationship does not exist.

        Return the label of the town judge if the town judge exists and can be
        identified, or return -1 otherwise.

        :param int n: number of people
        :param list[list[int]] trust: trust relationships of people in town
        :returns int judge_label: label of the town judge

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 98.77%
        """
        trust_list = {key: 0 for key in range(1, n + 1)}
        judge_label = -1

        for person, judge in trust:
            if person in trust_list:
                trust_list.pop(person)

            if judge in trust_list:
                trust_list[judge] += 1

        for person, trust_score in trust_list.items():
            if trust_score == n - 1:
                judge_label = person

        return judge_label if len(trust_list) == 1 else -1
