# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """
        Finds the intersection node of two singly linked lists, if it exists.

        Args:
            headA (Optional[ListNode]): The head of the first singly linked list.
            headB (Optional[ListNode]): The head of the second singly linked list.

        Returns:
            Optional[ListNode]: The intersection node, or None if the lists do not intersect.

        Example:
            Input:
                List A: 4 -> 1 \
                                8 -> 4 -> 5
                       5 -> 6 /
                List B:
            Output: Node with value 8

        Time Complexity: O(m + n), where m and n are the lengths of the two lists.
        Space Complexity: O(1)

        LeetCode: Beats 99.40% of submissions
        """
        pA, pB = headA, headB

        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA
