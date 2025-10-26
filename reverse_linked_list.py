# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.

        Args:
            head (Optional[ListNode]): Head node of the singly linked list.

        Returns:
            Optional[ListNode]: Head node of the reversed linked list.

        Example:
            Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
            Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
