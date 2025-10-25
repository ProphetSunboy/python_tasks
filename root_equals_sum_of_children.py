# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree with exactly 3 nodes (the root, its left child, and its right child),
        return True if the value of the root is equal to the sum of the values of its two children;
        return False otherwise.

        Args:
            root (Optional[TreeNode]): Root of the binary tree with exactly 3 nodes.

        Returns:
            bool: True if root.val == root.left.val + root.right.val, False otherwise.

        Example:
            >>> root = TreeNode(10, TreeNode(4), TreeNode(6))
            >>> checkTree(root)
            True

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return root.val == root.left.val + root.right.val
