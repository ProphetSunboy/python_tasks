class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        """
        Given a list of integers energy where each element represents a magician's energy (positive or negative)
        and an integer k, determines the maximum total energy that can be collected in a mystic dungeon.

        Rules:
            - You may start at any magician (index).
            - Upon absorbing energy at index i, you are immediately teleported to index i + k.
            - You continue this process until you reach an index i where i + k is outside the list bounds.
            - At each stop, you must absorb that magician's energy, regardless of whether it is positive or negative.

        Args:
            energy (List[int]): A list where each element is the energy value of a magician.
            k (int): The fixed jump length after absorbing energy from a magician.

        Returns:
            int: The maximum possible total energy that can be gained by any valid starting position.

        Example:
            >>> maximumEnergy([5, -2, 3, 1, -1], 2)
            7

        Time Complexity: O(n)
        Space Complexity: O(n)

        LeetCode: Beats 90% of submissions
        """
        n = len(energy)
        dp = energy[:]

        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] += dp[i + k]

        return max(dp)
