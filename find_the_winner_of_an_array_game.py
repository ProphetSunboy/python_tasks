class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        """
        Given an integer list arr of distinct integers and an integer k.

        A game will be played between the first two elements of the list
        (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0]
        with arr[1], the larger integer wins and remains at position 0, and the
        smaller integer moves to the end of the list. The game ends when an
        integer wins k consecutive rounds.

        Return the integer which will win the game.

        It is guaranteed that there will be a winner of the game.

        :param list[int] arr: integer list of distinct integers
        :param int k: integer
        :returns int curr: integer which will win the game

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 100%
        """
        if k >= len(arr) - 1:
            return max(arr)

        queue = collections.deque(arr)
        curr = queue.popleft()
        cons_score = 0

        while cons_score < k:
            val = queue.popleft()

            if curr > val:
                cons_score += 1
                queue.append(val)
            else:
                cons_score = 1
                queue.append(curr)
                curr = val

        return curr
