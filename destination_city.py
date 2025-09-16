class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        Given a list 'paths', where each element paths[i] = [cityA, cityB] represents
        a direct path from cityA to cityB, return the destination city—i.e., the city with no outgoing paths.

        It is guaranteed that the graph forms a straight line (no loops), so there
        will be exactly one destination city.

        Args:
            paths (List[List[str]]): List of direct city-to-city paths.

        Returns:
            str: The destination city with no outgoing path.

        Example:
            >>> destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
            'Sao Paulo'

        Time Complexity: O(n), where n is the number of paths.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        cities = {}

        for city_a, city_b in paths:
            cities[city_a] = 1
            cities[city_b] = cities.get(city_b, 0)

        for city, val in cities.items():
            if val == 0:
                return city
