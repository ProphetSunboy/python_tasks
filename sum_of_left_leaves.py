# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Returns the sum of all left leaves in a binary tree.

        A leaf is a node with no children. A left leaf is a leaf that is the left child of its parent.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The sum of all left leaf node values.

        Example:
            For the tree:
                3
               / \
              9  20
                /  \
               15   7
            sumOfLeftLeaves(root) returns 24 (9 + 15).

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (recursion stack).

        LeetCode: Beats 100% of submissions
        """
        self.left_leaves = 0

        def dfs(node):
            if not node:
                return

            if node.left:
                if not (node.left.left or node.left.right):
                    self.left_leaves += node.left.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.left_leaves
