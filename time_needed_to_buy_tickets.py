class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        Calculates the total time required for the person at position k to finish buying all their tickets.

        There are n people in a queue, represented by the list `tickets`, where
        tickets[i] is the number of tickets the i-th person wants to buy.
        Each person can buy only one ticket at a time and must rejoin the end of
        the line if they have more tickets to buy.
        The process continues until the person at position k has bought all their tickets.

        Args:
            tickets (List[int]): List where tickets[i] is the number of tickets the i-th person wants to buy.
            k (int): The index of the person whose total time to finish buying tickets is to be calculated.

        Returns:
            int: The total time (in seconds) for the person at position k to finish buying all their tickets.

        Example:
            >>> timeRequiredToBuy([2,3,2], 2)
            6
            >>> timeRequiredToBuy([5,1,1,1], 0)
            8

        Time Complexity: O(n), where n is the number of people in the queue.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        target = tickets[k]
        time = 0

        for i, t in enumerate(tickets):
            if i <= k:
                time += min(t, target)
            else:
                time += min(t, target - 1)

        return time
