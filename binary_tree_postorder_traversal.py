# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return the postorder traversal of a binary tree's node values.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[int]: A list containing the node values in postorder (left, right, root).

        Example:
            Given the binary tree:
                1
                 \
                  2
                 /
                3
            
            postorderTraversal(root) returns [3, 2, 1]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

        LeetCode: Beats 100% of submissions
        """
        self.res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            self.res.append(node.val)

        dfs(root)

        return self.res
