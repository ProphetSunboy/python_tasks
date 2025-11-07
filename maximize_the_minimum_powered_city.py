class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        """
        Returns the maximum possible minimum power among all cities after optimally
        building up to k additional power stations.

        Given:
        - stations: List[int], where stations[i] is the number of power stations in the ith city.
        - r: int, the range of each power station (each station at city i covers all cities j with |i - j| <= r).
        - k: int, the maximum number of new stations that can be built in any cities.

        A city's power is the total number of power stations within range
        (including those in the city itself).

        The goal is to choose locations for the k new stations such that the
        minimum power among all cities is maximized.

        Returns:
            int: The largest possible minimum power among all cities after
            optimally building up to k additional stations.

        Time Complexity: O(n log S), where n is the number of cities and S is the
        search range for the minimum power (up to sum(stations) + k).
        Space Complexity: O(n), used for prefix sum and difference lists.
        """
        n = len(stations)
        cnt = [0] * (n + 1)

        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            cnt[left] += stations[i]
            cnt[right] -= stations[i]

        def check(val: int) -> bool:
            diff = cnt.copy()
            total = 0
            remaining = k

            for i in range(n):
                total += diff[i]
                if total < val:
                    add = val - total
                    if remaining < add:
                        return False
                    remaining -= add
                    end = min(n, i + 2 * r + 1)
                    diff[end] -= add
                    total += add
            return True

        lo, hi = min(stations), sum(stations) + k
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res
