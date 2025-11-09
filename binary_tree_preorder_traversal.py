# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform a preorder traversal of a binary tree and return a list of node values.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: Node values in preorder (root, left, right) traversal order.

        Example:
            Given the binary tree:
                1
                 \
                  2
                 /
                3

            preorderTraversal(root) returns [1, 2, 3]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

        LeetCode: Beats 100% of submissions
        """
        self.res = []

        def traverse(node):
            if not node:
                return

            self.res.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return self.res
