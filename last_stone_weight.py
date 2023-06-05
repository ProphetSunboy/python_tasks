class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Given an array of integers stones where stones[i] is the weight of the
        ith stone.

        Rules:
        We are playing a game with the stones. On each turn, we choose the
        heaviest two stones and smash them together. Suppose the heaviest two
        stones have weights x and y with x <= y. The result of this smash is:

        If x == y, both stones are destroyed, and
        If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

        At the end of the game, there is at most one stone left.

        Return the weight of the last remaining stone. If there are no stones
        left, return 0.
        """
        s_weights = sorted(stones, reverse=True)
        while len(s_weights) > 1:
            if s_weights[0] == s_weights[1]:
                s_weights = s_weights[2:]
            else:
                s_weights[0] -= s_weights[1]
                s_weights.pop(1)
                s_weights = sorted(s_weights, reverse=True)
        return s_weights[0] if s_weights else 0