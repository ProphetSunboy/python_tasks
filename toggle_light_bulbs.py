class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        """
        Given a list bulbs of integers between 1 and 100, toggle the respective
        bulbs.

        There are 100 light bulbs numbered from 1 to 100, all initially
        switched off.
        For each element in bulbs:
            - If the bulbs[i] light bulb is off, switch it on.
            - If it is on, switch it off.

        Returns the list of light bulbs that are on at the end, sorted in
        ascending order.
        Returns an empty list if no bulbs are on.

        Args:
            bulbs (list[int]): The list of bulbs to toggle.

        Returns:
            list[int]: The bulbs that are on at the end, sorted.

        Example:
            Input: bulbs = [1, 2, 3, 2]
            Output: [1, 3]

        Time Complexity: O(n), where n is the length of bulbs.
        Space Complexity: O(1), since the number of bulbs is constant (100).

        LeetCode: Beats 100% of submissions
        """
        bulbs_on = defaultdict(bool)

        for bulb in bulbs:
            bulbs_on[bulb] = not bulbs_on[bulb]

        return sorted([bulb for bulb, on in bulbs_on.items() if on])
