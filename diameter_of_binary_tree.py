# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the diameter of a binary tree.

        The diameter is defined as the length (number of edges) of the longest
        path between any two nodes in the tree, which may or may not pass
        through the root.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The length of the tree's diameter.

        Example:
            Input: root = [3,9,20,None,None,15,7]
            Output: 3   # The longest path is 15-20-3-9 or 7-20-3-9 (length is 3 edges)

        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

        LeetCode: Beats 97.15% of submissions
        """
        self.diameter = 0

        def traverse(node, curr):
            if not node:
                return curr - 1

            left = traverse(node.left, curr + 1)
            right = traverse(node.right, curr + 1)

            if left + right - 2 * curr > self.diameter:
                self.diameter = left + right - 2 * curr

            return max(left, right)

        traverse(root, 0)

        return self.diameter
