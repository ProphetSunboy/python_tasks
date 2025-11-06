# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the inorder traversal of the values of a binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: List of node values in inorder (left-root-right) sequence.

        Example:
            Given the following tree:
                1
                 \
                  2
                 /
                3
            inorderTraversal(root) returns [1, 3, 2]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

        LeetCode: Beats 100% of submissions
        """
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res
