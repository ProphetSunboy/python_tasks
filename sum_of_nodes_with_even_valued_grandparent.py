# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        """
        Returns the sum of values of all nodes in the binary tree whose grandparent node has an even value.
        A grandparent of a node is defined as the parent of its parent, if it exists.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The sum of values of nodes with even-valued grandparent nodes.

        Example:
            Input: root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
            Output: 18
            (The nodes with even-valued grandparent are 2, 7, 1, 3, 5, whose sum is 18.)

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree due to recursion stack.

        LeetCode: Beats 98.34% of submissions
        """
        self.even_sum = 0

        def traverse(node):
            if not node:
                return

            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        self.even_sum += node.left.left.val
                    if node.left.right:
                        self.even_sum += node.left.right.val
                if node.right:
                    if node.right.left:
                        self.even_sum += node.right.left.val
                    if node.right.right:
                        self.even_sum += node.right.right.val

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return self.even_sum
