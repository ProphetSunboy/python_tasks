# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determines whether two binary trees are the same.

        Two binary trees are considered the same if they are structurally identical
        and the corresponding nodes have the same values.

        Args:
            p (Optional[TreeNode]): Root of the first binary tree.
            q (Optional[TreeNode]): Root of the second binary tree.

        Returns:
            bool: True if the trees are the same, False otherwise.

        Example:
            Given two trees:

                1      1
               / \    / \
              2   3  2   3

            isSameTree(p, q) returns True.

            Given two trees:

                1      1
               /        \
              2          2

            isSameTree(p, q) returns False.

        Time Complexity: O(n), where n is the number of nodes in the trees.
        Space Complexity: O(h), where h is the height of the trees (due to the recursion stack).

        LeetCode: Beats 100% of submissions
        """
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
