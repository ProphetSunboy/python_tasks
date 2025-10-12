class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        """
        Given an integer list `cost` of length n, representing the cost to swap
        places with each person at positions 0 to n-1 in a line of n+1 people
        (positions 0 to n). You begin at position n.

        You can move forward in the line by swapping with people in front of you,
        paying their specified cost (`cost[i]`). Swapping with people behind you is free.

        Returns a list `answer` of length n, where `answer[i]` is the minimum
        total cost required to reach position `i` from the end.

        Args:
            cost (List[int]): List of costs for swapping with each person.

        Returns:
            List[int]: The minimum cost to reach each position from the end.

        Example:
            >>> minCosts([2, 8, 2, 6, 12])
            [2, 2, 2, 2, 2]

        Time Complexity: O(n), where n is the length of the cost list.
        Space Complexity: O(n) for the answer list.

        LeetCode: Beats 100% of submissions
        """
        answer = [cost[0]]
        curr_min = cost[0]

        for i in range(1, len(cost)):
            curr_min = min(curr_min, cost[i])
            answer.append(curr_min)

        return answer
