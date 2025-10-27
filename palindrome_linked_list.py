# First solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Determines whether a singly-linked list is a palindrome.

        Args:
            head (Optional[ListNode]): The head node of the singly linked list.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.

        Example:
            >>> # Given the linked list: 1 -> 2 -> 2 -> 1
            >>> isPalindrome(head)
            True
            >>> # Given the linked list: 1 -> 2
            >>> isPalindrome(head)
            False

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(n), for storing node values.

        LeetCode: Beats 95.42% of submissions
        """
        values = []
        curr = head

        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        return values == values[::-1]


# Second solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Determines whether a singly-linked list is a palindrome.

        Args:
            head (Optional[ListNode]): The head node of the singly linked list.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.

        Example:
            >>> # Given the linked list: 1 -> 2 -> 2 -> 1
            >>> isPalindrome(head)
            True
            >>> # Given the linked list: 1 -> 2
            >>> isPalindrome(head)
            False

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(n), for storing node values.

        LeetCode: Beats 95.42% of submissions
        """
        values = []
        curr = head

        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        for i in range(len(values) // 2):
            if values[i] != values[-i - 1]:
                return False

        return True
