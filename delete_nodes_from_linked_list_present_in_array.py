# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Removes nodes from a singly linked list if their value is present in a given list.

        Args:
            nums (List[int]): List of integers. Nodes with values in this list will be removed from the linked list.
            head (Optional[ListNode]): The head of the singly linked list.

        Returns:
            Optional[ListNode]: The head of the modified linked list after removals.

        Example:
            >>> # Remove nodes whose values are in [6, 3]
            >>> # Input list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
            >>> Solution().modifiedList([6, 3], ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))
            ListNode(1, ListNode(2, ListNode(4, ListNode(5))))

        Time Complexity: O(n + m), where n is the number of nodes in the linked list and m is the number of elements in nums.
        Space Complexity: O(m), for storing nums as a set.

        LeetCode: Beats 90.33% of submissions
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        nums_s = set(nums)

        while curr.next:
            if curr.next.val in nums_s:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
