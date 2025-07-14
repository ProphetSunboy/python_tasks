class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        """Determines the best possible poker hand from the given ranks and suits of 5 cards.

        Poker hand rankings from best to worst:
            - "Flush": All five cards have the same suit.
            - "Three of a Kind": Three cards have the same rank.
            - "Pair": Two cards have the same rank.
            - "High Card": None of the above.

        Args:
            ranks (list[int]): List of 5 integers representing the rank of each card.
            suits (list[str]): List of 5 characters representing the suit of each card.

        Returns:
            str: The best type of poker hand ("Flush", "Three of a Kind", "Pair", or "High Card").

        Example:
            >>> bestHand([13,2,3,1,9], ["a","a","a","a","a"])
            'Flush'
            >>> bestHand([4,4,2,4,4], ["d","a","a","b","c"])
            'Three of a Kind'
            >>> bestHand([10,10,2,12,9], ["a","b","c","a","d"])
            'Pair'
            >>> bestHand([2,3,4,5,6], ["a","b","c","d","e"])
            'High Card'

        Time complexity: O(n), where n is the number of cards (5).
        Space complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        flush = True

        for i in range(1, len(suits)):
            if suits[i] != suits[0]:
                flush = False
                break

        if flush:
            return "Flush"

        ranks_c = Counter(ranks)
        max_freq = max(ranks_c.values())

        if max_freq >= 3:
            return "Three of a Kind"
        elif max_freq == 2:
            return "Pair"

        return "High Card"
