# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree where each node's value is 0 or 1, each
        root-to-leaf path represents a binary number, with the root as the most
        significant bit.
        This function returns the sum of all the numbers that can be formed from
        root-to-leaf paths.

        For example, the path 0 -> 1 -> 1 -> 0 -> 1 represents the binary number 01101 (decimal 13).
        For every leaf in the tree, consider the binary number represented by
        the path from the root to that leaf and sum them.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The sum of all root-to-leaf binary numbers.

        Example:
            Given the tree:
                1
               / \
              0   1
             / \ / \
            0  1 0  1

            There are four root-to-leaf paths:
                100 (4), 101 (5), 110 (6), 111 (7)
                Their sum is 4 + 5 + 6 + 7 = 22.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (recursive stack).

        LeetCode: Beats 100% of submissions.
        """

        def dfs(node, current):
            if not node:
                return 0

            current = (current << 1) | node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)
