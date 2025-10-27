# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted singly-linked lists into a new sorted linked list.

        You are given the heads of two sorted linked lists, list1 and list2.
        The lists should be merged by splicing together the nodes from the original
        lists to create a single, sorted linked list.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.

        Example:
            >>> # list1: 1 -> 2 -> 4
            >>> # list2: 1 -> 3 -> 4
            >>> merged = mergeTwoLists(list1, list2)
            >>> # merged: 1 -> 1 -> 2 -> 3 -> 4 -> 4

        Time Complexity: O(m + n), where m and n are the lengths of the two lists.
        Space Complexity: O(1) (excluding the output list nodes, which are reused from the inputs).

        LeetCode: Beats 100% of submissions
        """
        dummy = ListNode()
        curr = dummy

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        curr.next = curr1 if curr1 else curr2

        return dummy.next
