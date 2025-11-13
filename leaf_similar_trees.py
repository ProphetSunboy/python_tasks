# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Determines whether two binary trees are leaf-similar.

        Two binary trees are leaf-similar if the sequence of their leaf node values,
        read from left to right, is identical.

        Args:
            root1 (Optional[TreeNode]): The root node of the first binary tree.
            root2 (Optional[TreeNode]): The root node of the second binary tree.

        Returns:
            bool: True if the leaf value sequences of both trees are the same, False otherwise.

        Example:
            Input: root1 = [3,5,1,6,2,9,8,None,None,7,4],
            root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
            Output: True

        Time Complexity: O(n), where n is the total number of nodes in both trees.
        Space Complexity: O(h), where h is the height of the tree (for recursion stack).

        LeetCode: Beats 100% of submissions
        """
        leaves1 = []
        leaves2 = []

        def traverse(node, leaves):
            if not node:
                return

            if not node.left and not node.right:
                leaves.append(node.val)

            traverse(node.left, leaves)
            traverse(node.right, leaves)

            return leaves

        return traverse(root1, leaves1) == traverse(root2, leaves2)
