class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        """Finds the maximum number of matchings between players and trainers based on their abilities and capacities.

        Each player can be matched with at most one trainer, and each trainer with
        at most one player. A player can be matched with a trainer if the player's
        ability is less than or equal to the trainer's training capacity.

        Args:
            players (list[int]): List of player abilities.
            trainers (list[int]): List of trainer capacities.

        Returns:
            int: The maximum number of valid player-trainer matchings.

        Example:
            >>> matchPlayersAndTrainers([4,7,9], [8,2,5,8])
            2
            >>> matchPlayersAndTrainers([1,1,1], [10])
            1

        Time complexity: O(n log n + m log m), where n is the number of players and m is the number of trainers (due to sorting).
        Space complexity: O(1), not counting input and output.
        """
        matchings = 0
        i, j = 0, 0
        players.sort()
        trainers.sort()

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                matchings += 1
                i += 1
                j += 1
            else:
                j += 1

        return matchings
