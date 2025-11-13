# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree.

        Each node's left and right children are swapped recursively,
        producing the mirror image of the original tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            Optional[TreeNode]: The root node of the inverted binary tree.

        Example:
            Input:  root = [4,2,7,1,3,6,9]
            Output: [4,7,2,9,6,3,1]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (for recursion stack).

        LeetCode: Beats 100% of submissions
        """

        def invert(node):
            if not node:
                return

            node.left, node.right = node.right, node.left

            invert(node.left)
            invert(node.right)

            return node

        return invert(root)
