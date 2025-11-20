# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Given the head of a singly-linked list, insert a new node between every
        pair of adjacent nodes.
        The value of the new node should be the greatest common divisor (GCD)
        of the values of its two neighboring nodes.

        Args:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            Optional[ListNode]: The head of the modified linked list after
            inserting GCD nodes between all adjacent nodes.

        Example:
            Input: head = [18,6,10,3]
            Output: [18,6,6,2,10,1,3]
              # Explanation: GCD(18,6)=6, GCD(6,10)=2, GCD(10,3)=1

        Time Complexity: O(n), where n is the length of the linked list.
        Space Complexity: O(1), modifies the list in-place.

        LeetCode: Beats 98.60% of submissions
        """
        curr = head

        while curr.next:
            curr_gcd = gcd(curr.val, curr.next.val)
            curr.next = ListNode(curr_gcd, curr.next)
            curr = curr.next.next

        return head
