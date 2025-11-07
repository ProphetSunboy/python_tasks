# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Counts the number of nodes in a complete binary tree.

        A complete binary tree is a binary tree in which every level, except possibly
        the last, is completely filled, and all nodes in the last level are as far
        left as possible.

        Args:
            root (Optional[TreeNode]): The root node of the complete binary tree.

        Returns:
            int: The total number of nodes in the tree.


        Example:
            For the tree:
                1
               / \
              2   3
             / \  /
            4  5 6

            countNodes(root) returns 6.

        Time Complexity: O((n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (recursion stack).
        """
        self.nodes = 0

        def dfs(node):
            if not node:
                return

            self.nodes += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.nodes
