class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Given a string tiles consisting of uppercase English letters,
        return the number of possible non-empty sequences of letters
        you can make using the letters printed on those tiles.

        Args:
            tiles (str): The string of available letter tiles.

        Returns:
            int: The count of all possible non-empty sequences.

        Example:
            Input:  tiles = "AAB"
            Output: 8

        Time Complexity: O(K * N^2), where N is the total number of tiles and K
        is the number of unique characters.
        Space Complexity: O(N), for the dynamic programming list.

        LeetCode: Beats 100% of submissions
        """
        counts = list(Counter(tiles).values())
        n = len(tiles)

        dp = [0] * (n + 1)
        dp[0] = 1

        total_len = 0
        for count in counts:
            new_dp = [0] * (n + 1)

            for i in range(total_len + 1):
                for j in range(count + 1):
                    new_dp[i + j] += dp[i] * comb(i + j, j)
            dp = new_dp
            total_len += count

        return sum(dp[1:])
