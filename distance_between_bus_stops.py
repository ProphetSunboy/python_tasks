class Solution:
    def distanceBetweenBusStops(
        self, distance: list[int], start: int, destination: int
    ) -> int:
        """
        A bus has n stops numbered from 0 to n - 1 that form a circle. We know
        the distance between all pairs of neighboring stops where distance[i] is
        the distance between the stops number i and (i + 1) % n.

        The bus goes along both directions i.e. clockwise and counterclockwise.

        Return the shortest distance between the given start and destination
        stops.

        LeetCode Beats 99.01%
        """
        clock = 0
        c_clock = 0

        for i in range(start, start + len(distance)):
            if i % len(distance) == destination:
                break

            clock += distance[i % len(distance)]

        for i in range(start, destination - len(distance), -1):
            if i % len(distance) == destination:
                break
            c_clock += distance[i - 1]

        return min(clock, c_clock)
