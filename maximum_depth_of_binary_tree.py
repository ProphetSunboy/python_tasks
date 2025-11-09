# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum depth of a binary tree.

        The maximum depth is defined as the number of nodes
        along the longest path from the root node down to the farthest leaf node.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum depth of the tree.

        Example:
            Given the following binary tree:
                1
                 \
                  2
                 /
                3

            maxDepth(root) returns 3.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

        LeetCode: Beats 100% of submissions
        """

        def traverse(node, curr):
            if not node:
                return curr

            curr += 1

            return max(traverse(node.left, curr), traverse(node.right, curr))

        return traverse(root, 0)
