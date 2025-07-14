class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """Given the head of a singly-linked list where each node contains a binary digit (0 or 1),
        this function returns the decimal value represented by the linked list.

        The most significant bit is at the head of the linked list.

        Args:
            head (Optional[ListNode]): The head node of the singly-linked list.

        Returns:
            int: The decimal value of the binary number represented by the linked list.

        Example:
            For a linked list 1 -> 0 -> 1:
                The binary number is 101, which equals 5 in decimal.
                >>> getDecimalValue(head)  # where head is the start of 1->0->1
                5

        Time complexity: O(n), where n is the number of nodes in the linked list.
        Space complexity: O(n), due to the list used to collect node values.

        LeetCode: Beats 100% of submissions
        """
        num = []

        while head.next:
            num.append(head.val)
            head = head.next

        num.append(head.val)
        b_num = "0b" + "".join(map(str, num))

        return int(b_num, 2)
