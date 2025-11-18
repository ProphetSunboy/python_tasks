# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced.

        A binary tree is height-balanced if, for every node, the depths of its
        left and right subtrees differ by no more than one.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            bool: True if the tree is height-balanced, False otherwise.

        Example:
            Input: root = [3,9,20,None,None,15,7]
            Output: True

        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(h), where h is the height of the tree (recursion stack).

        LeetCode: Beats 100% of submissions
        """

        def traverse(node, curr):
            if not node:
                return curr

            left = traverse(node.left, curr + 1)
            right = traverse(node.right, curr + 1)

            if abs(left - right) > 1:
                return 10**5

            return max(left, right)

        return traverse(root, 0) < 10**5
