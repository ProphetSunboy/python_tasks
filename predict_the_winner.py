class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        """
        You are given an integer array nums. Two players are playing a game with
        this array: player 1 and player 2.

        Player 1 and player 2 take turns, with player 1 starting first. Both
        players start the game with a score of 0. At each turn, the player
        takes one of the numbers from either end of the array (i.e., nums[0] or
        nums[nums.length - 1]) which reduces the size of the array by 1.
        The player adds the chosen number to their score. The game ends when
        there are no more elements in the array.

        Return True if Player 1 can win the game. If the scores of both players
        are equal, then player 1 is still the winner, and you should also
        return True. You may assume that both players are playing optimally.

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.39%
        """
        players_scores = [0, 0]
        i = 0

        while nums:
            if len(nums) > 3:
                if nums[1] - nums[0] <= nums[-2] - nums[-1]:
                    players_scores[i % 2] += nums[0]
                    nums.pop(0)
                else:
                    players_scores[i % 2] += nums[-1]
                    nums.pop()
            else:
                players_scores[i % 2] += max(nums[0], nums[-1])
                if nums[0] > nums[-1]:
                    nums.pop(0)
                else:
                    nums.pop()

            i += 1

        return players_scores[0] >= players_scores[1]
