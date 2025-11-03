# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a Binary Search Tree (BST), returns the minimum difference
        between the values of any two distinct nodes in the tree.

        An in-order traversal is used to visit nodes in ascending order. 
        The minimum difference is always found between consecutive nodes during this traversal.

        Args:
            root (Optional[TreeNode]): The root node of the BST.

        Returns:
            int: The minimum absolute difference between values of any two nodes.

        Example:
            >>> # For tree:   4
            >>> #           / \
            >>> #          2   6
            >>> #         / \
            >>> #        1   3
            >>> minDiffInBST(root)
            1

        Time Complexity: O(n), where n is the number of nodes in the BST.
        Space Complexity: O(h), where h is the height of the BST (due to recursion stack).

        LeetCode: Beats 100% of submissions
        """
        self.prev = None
        self.min_diff = float("inf")

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev is not None:
                diff = node.val - self.prev
                self.min_diff = min(self.min_diff, diff)
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff
