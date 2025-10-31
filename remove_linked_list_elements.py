# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Removes all nodes with a specified value from a singly linked list.

        Args:
            head (Optional[ListNode]): The head of the singly linked list.
            val (int): The value to remove from the list.

        Returns:
            Optional[ListNode]: The head of the updated linked list after removal.

        Example:
            >>> # Removes all 6's from the list: 1->2->6->3->4->5->6 becomes 1->2->3->4->5
            >>> removeElements(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6)
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1), as removal is done in place.

        LeetCode: Beats 100% of submissions
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
