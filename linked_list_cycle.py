class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has
        a cycle in it.

        Return True if there is a cycle in the linked list. Otherwise, return
        False.

        There is a cycle in a linked list if there is some node in the list that
        can be reached again by continuously following the next pointer.


        :param Optional[ListNode] head: head of the linked list
        :returns bool cycle: True if there is cycle in the linked, otherwise False

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 97.64%
        """
        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast == None or fast.next == None:
            return False

        while head != slow:
            head = head.next
            slow = slow.next

        return True
