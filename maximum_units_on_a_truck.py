class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        """Calculates the maximum total number of units that can be loaded onto a truck.

        You are given:
            - boxTypes: A list of lists, where each inner list is of the form [numberOfBoxes, numberOfUnitsPerBox].
            - truckSize: An integer representing the maximum number of boxes the truck can carry.

        The goal is to select boxes (of any type) such that the total number of boxes does not exceed truckSize,
        and the total number of units loaded onto the truck is maximized.

        Args:
            boxTypes (list[list[int]]): Each element is [numberOfBoxes, numberOfUnitsPerBox].
            truckSize (int): Maximum number of boxes the truck can carry.

        Returns:
            int: The maximum total number of units that can be put on the truck.

        Example:
            >>> maximumUnits([[1,3],[2,2],[3,1]], 4)
            8
            >>> maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)
            91

        Time complexity: O(n log n), where n is the number of box types (due to sorting).
        Space complexity: O(1) (ignoring input storage).

        LeetCode: Beats 100% of submissions
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        max_units = 0
        i = 0

        while truckSize > 0 and i < len(boxTypes):
            if boxTypes[i][0] <= truckSize:
                max_units += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                max_units += truckSize * boxTypes[i][1]
                truckSize -= truckSize

            i += 1

        return max_units
