class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        Simulates the process of avoiding floods in lakes given a sequence of rain and dry days.

        You are given an integer list `rains` where:
            - rains[i] > 0: It rains over lake rains[i] on the i-th day.
            - rains[i] == 0: No rain on the i-th day; you may choose one lake to dry.

        The goal is to avoid flooding any lake. If it rains over a lake that is already full, a flood occurs.
        On dry days, you can choose any lake to dry (making it empty if it was full; no effect if already empty).

        Returns a list `ans` of length equal to `rains`:
            - ans[i] == -1 if rains[i] > 0 (it rained that day).
            - ans[i] == x if rains[i] == 0, where x is the lake you chose to dry on the i-th day.

        If it is impossible to avoid a flood, returns an empty list.
        If there are multiple valid answers, any one is acceptable.

        Args:
            rains (List[int]): The sequence of rain and dry days.

        Returns:
            List[int]: The sequence of actions taken to avoid floods, or an empty list if impossible.

        Example:
            >>> avoidFlood([1,2,0,0,2,1])
            [-1, -1, 2, 1, -1, -1]
            >>> avoidFlood([1,2,0,1,2])
            []

        Time Complexity: O(n^2) in the worst case (due to searching for dry days).
        Space Complexity: O(n), where n is the length of rains.
        """
        full = dict()
        dry_days = []
        ans = [-1] * len(rains)

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                ans[i] = 1
            else:
                if lake in full:
                    last_rain = full[lake]
                    pos = -1
                    for j, dry_day in enumerate(dry_days):
                        if dry_day > last_rain:
                            pos = j
                            break
                    if pos == -1:
                        return []
                    dry_day = dry_days.pop(pos)
                    ans[dry_day] = lake
                full[lake] = i
                ans[i] = -1

        return ans
