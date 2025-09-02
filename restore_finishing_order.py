class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        """
        You are given an integer list order of length n and an integer list friends.

        Order contains every integer from 1 to n exactly once, representing the IDs
        of the participants of a race in their finishing order.
        Friends contains the IDs of your friends in the race sorted in strictly
        increasing order. Each ID in friends is guaranteed to appear in the order list.
        Return a list containing your friends' IDs in their finishing order.

        Args:
            order (list[int]): The list of IDs in the finishing order.
            friends (list[int]): The list of your friends' IDs.

        Returns:
            list[int]: The list of your friends' IDs in their finishing order.

        Example:
            >>> recoverOrder([3,1,2,5,4], [1,3,4])
            [3, 1, 4]

        Time Complexity: O(n), where n is the length of order.
        Space Complexity: O(f), where f is the number of friends.

        LeetCode: Beats 100% of submissions
        """
        finishing_order = []

        for i in order:
            if i in friends:
                finishing_order.append(i)

        return finishing_order
