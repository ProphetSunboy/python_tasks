# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Removes duplicates from a sorted singly linked list so that each element appears only once.

        Args:
            head (Optional[ListNode]): The head of the sorted singly linked list.

        Returns:
            Optional[ListNode]: The head of the linked list after removing duplicates.

        Example:
            >>> # Input list: 1 -> 1 -> 2 -> 3 -> 3
            >>> deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))
            ListNode(1, ListNode(2, ListNode(3)))

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(1), in-place modification.

        LeetCode: Beats 100% of submissions
        """
        dummy = ListNode(-101)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
