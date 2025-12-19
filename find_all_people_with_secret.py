class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int):
        """
        Determines all people who ultimately know a secret after a series of meetings.

        Problem:
            - There are n people labeled from 0 to n-1.
            - Person 0 initially knows a secret and immediately shares it with firstPerson at time 0.
            - Meetings is a list of [xi, yi, timei] where xi and yi meet at timei.
            - If either person in a meeting knows the secret at the meeting time, both will know the secret instantly.
            - Secrets can be shared within the same time frame with transitive meetings.

        Args:
            n (int): Number of people.
            meetings (List[List[int]]): Each element is [xi, yi, timei], where xi and yi meet at timei.
            firstPerson (int): The initial recipient of the secret from person 0 at time 0.

        Returns:
            List[int]: All people who know the secret after all meetings have occurred (order does not matter).

        Example:
            Input: n = 4, meetings = [[1,2,1],[2,3,1],[0,1,0]], firstPerson = 1
            Output: [0,1,2,3]

        Time Complexity: O(M log M + M + N), where M = number of meetings.
        Space Complexity: O(N + M).
        """
        from collections import defaultdict

        meetings.sort(key=lambda x: x[2])

        knows = [False] * n
        knows[0] = knows[firstPerson] = True

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            people = set()

            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                people.add(x)
                people.add(y)
                i += 1

            component_has_secret = defaultdict(bool)
            for p in people:
                if knows[p]:
                    component_has_secret[find(p)] = True

            for p in people:
                if component_has_secret[find(p)]:
                    knows[p] = True

            for p in people:
                parent[p] = p

        return [i for i in range(n) if knows[i]]
