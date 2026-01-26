class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        """
        Calculate the minimum number of minutes needed to pick up all the garbage.

        Each house contains a string of garbage types:
            - 'M': metal
            - 'P': paper
            - 'G': glass

        Picking up one unit of any type of garbage takes 1 minute.

        There are three garbage trucks, each responsible for picking up one type of
        garbage. Each truck starts at house 0 and must visit houses in order, but only
        needs to visit houses containing its garbage type. Only one truck may be used at
        any time; while one truck is driving or collecting, others cannot act.

        Args:
            garbage (List[str]): A list where garbage[i] is a string representing
                the assortment of garbage at the i-th house.
            travel (List[int]): A list where travel[i] is the number of minutes
                needed to go from house i to house i + 1.

        Returns:
            int: The minimum number of minutes to pick up all garbage.

        Example:
            Input: garbage = ["G", "P", "GP", "GG"], travel = [2, 4, 3]
            Output: 21

        Time Complexity: O(n), where n is the number of houses.
        Space Complexity: O(n), for prefix-sum calculation.
        """
        total_time = sum(len(house) for house in garbage)

        last_m = last_p = last_g = 0

        for i in range(len(garbage)):
            if "M" in garbage[i]:
                last_m = i
            if "P" in garbage[i]:
                last_p = i
            if "G" in garbage[i]:
                last_g = i

        travel_sums = [0] * len(garbage)
        current_sum = 0
        for i in range(len(travel)):
            current_sum += travel[i]
            travel_sums[i + 1] = current_sum

        total_time += travel_sums[last_m]
        total_time += travel_sums[last_p]
        total_time += travel_sums[last_g]

        return total_time
