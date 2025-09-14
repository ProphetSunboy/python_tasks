class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        """
        Given a 0-indexed integer list batteryPercentages of length n, representing
        the battery percentages of n devices:

        For each device i from 0 to n - 1, perform the following:
            - If batteryPercentages[i] > 0:
                - Increment the count of tested devices.
                - Decrease the battery percentage of all devices with indices j in [i + 1, n - 1] by 1,
                but not below 0 (i.e., batteryPercentages[j] = max(0, batteryPercentages[j] - 1)).
            - Otherwise, move to the next device.

        Return the total number of devices that are tested after performing all operations in order.

        Args:
            batteryPercentages (List[int]): The battery percentages of the devices.

        Returns:
            int: The number of devices that will be tested.

        Example:
            >>> countTestedDevices([1, 1, 2, 1, 3])
            3

        Time Complexity: O(n), where n is the number of devices.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        tested_devices = 0

        for perc in batteryPercentages:
            if perc - tested_devices > 0:
                tested_devices += 1

        return tested_devices
