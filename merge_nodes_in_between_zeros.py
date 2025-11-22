# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges nodes in between zeros in a linked list.

        Given the head of a linked list where each element is an integer, and
        the list contains sequences of values separated by nodes with value 0
        (including at the start and end), this function merges all nodes between
        every pair of consecutive zero nodes into a single node whose value is
        the sum of the merged values.
        All zero nodes are removed from the final list.

        Args:
            head (Optional[ListNode]): The head of the initial linked list.

        Returns:
            Optional[ListNode]: The head of the modified linked list after merging.

        Example:
            Input: head = [0,3,1,0,4,5,2,0]
            Output: [4,11]
            # Explanation:
            # The values between the first pair of zeros are [3,1], which sum to 4.
            # The values between the second pair are [4,5,2], which sum to 11.

        Time Complexity: O(n), where n is the number of nodes in the input list.
        Space Complexity: O(1), beyond the space for the new list.
        """
        curr = head.next
        dummy = ListNode(0)
        res = dummy

        curr_merge = 0
        while curr:
            if curr.val != 0:
                curr_merge += curr.val
            else:
                res.next = ListNode(curr_merge)
                res = res.next
                curr_merge = 0

            curr = curr.next

        return dummy.next
