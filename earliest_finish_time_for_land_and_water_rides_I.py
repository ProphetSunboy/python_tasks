class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        """
        Calculates the earliest possible finish time for a tourist to experience
        exactly one land ride and one water ride at a theme park, in either order.

        There are two categories of attractions:
            - Land rides: Each with its earliest possible boarding time (landStartTime[i]) and duration (landDuration[i]).
            - Water rides: Each with its earliest possible boarding time (waterStartTime[j]) and duration (waterDuration[j]).

        The tourist must choose one ride from each category, and may choose to do
        the land ride before the water ride or vice versa. The tourist may wait
        before starting a ride (but cannot board before its opening time).
        After finishing the first ride, the tourist may immediately board the second
        if it is open, or wait until it opens, and then complete it.

        Args:
            landStartTime (List[int]): Earliest boarding times for each land ride.
            landDuration (List[int]): Durations of each land ride.
            waterStartTime (List[int]): Earliest boarding times for each water ride.
            waterDuration (List[int]): Durations of each water ride.

        Returns:
            int: The minimum possible time at which both rides can be completed.

        Example:
            >>> earliestFinishTime([2,8], [4,1], [6], [3])
            9

        Time Complexity: O(n * m), where n is the number of land rides and m is the number of water rides.
        Space Complexity: O(1)
        """
        min_time = float("infinity")

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                curr_time = 0

                if landStartTime[i] < waterStartTime[j]:
                    curr_time += landStartTime[i] + landDuration[i]
                    if curr_time < waterStartTime[j]:
                        curr_time += waterStartTime[j] - curr_time
                    curr_time += waterDuration[j]
                else:
                    curr_time += waterStartTime[j] + waterDuration[j]
                    if curr_time < landStartTime[i]:
                        curr_time += landStartTime[i] - curr_time
                    curr_time += landDuration[i]

                if curr_time < min_time:
                    min_time = curr_time

        return min_time
