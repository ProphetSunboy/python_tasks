class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        Given an integer list deck where each card has a unique integer value,
        determine an initial ordering of the deck that will reveal the cards in
        increasing order by performing the following process:

            1. Take the top card of the deck, reveal it, and remove it from the deck.
            2. If there are still cards in the deck, put the next top card at the bottom of the deck.
            3. Repeat steps 1 and 2 until all cards are revealed.

        The first entry in the returned list will represent the top of the deck.

        Args:
            deck (List[int]): A list of integers representing unique cards.

        Returns:
            List[int]: An ordering of the deck that reveals cards in increasing order.

        Example:
            Input: deck = [17, 13, 11, 2, 3, 5, 7]
            Output: [2, 13, 3, 11, 5, 17, 7]

        Time Complexity: O(n log n), where n is the number of cards in the deck (due to sorting).
        Space Complexity: O(n), for constructing the result.

        LeetCode: Beats 100% of submissions
        """
        n = len(deck)
        deck.sort()

        index_queue = deque(range(n))
        result = [0] * n

        for card in deck:
            idx = index_queue.popleft()
            result[idx] = card

            if index_queue:
                index_queue.append(index_queue.popleft())

        return result
