# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Returns the middle node of a singly linked list.

        If there are two middle nodes (even-length list), returns the second one.

        Args:
            head (Optional[ListNode]): The head of the singly linked list.

        Returns:
            Optional[ListNode]: The middle node of the linked list.

        Example:
            >>> # For the list 1->2->3->4->5,
            >>> middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).val
            3
            >>> # For the list 1->2->3->4->5->6,
            >>> middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))).val
            4

        Time Complexity: O(n), where n is the length of the list.
        Space Complexity: O(n), due to storing nodes in a list.

        LeetCode: Beats 100% of submissions
        """
        nodes = []
        curr = head

        while curr is not None:
            nodes.append(curr)
            curr = curr.next

        return nodes[len(nodes) // 2]
