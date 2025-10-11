class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        """
        Calculates the maximum total damage a magician can deal by casting spells
        under strict casting constraints.

        Given a list of integers `power`, where each element represents the damage
        value of a spell (spells with the same damage value may occur multiple times):

            - Selecting a spell with damage value `d` prohibits selecting any spell
              with damage `d-2`, `d-1`, `d+1`, or `d+2`.
            - Each spell may be cast at most once.

        The goal is to maximize the sum of the selected spell damages subject to the rules above.

        Args:
            power (List[int]): List of integers representing spell damage values.

        Returns:
            int: The maximum total damage achievable with the spelled selection constraints.

        Example:
            >>> maximumTotalDamage([2, 3, 5, 7, 5, 3])
            13

        Time Complexity: O(N log N), where N is the number of unique damage values.
        Space Complexity: O(N)
        """
        freq = Counter(power)
        values = sorted(freq)

        n = len(values)
        dp = [0] * n

        for i in range(n):
            damage = values[i] * freq[values[i]]
            dp[i] = damage

            for j in range(i - 1, -1, -1):
                if abs(values[i] - values[j]) > 2:
                    dp[i] = max(dp[i], damage + dp[j])
                    break

            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])

        return max(dp)
