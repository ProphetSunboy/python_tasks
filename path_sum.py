# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Determines if the binary tree has a root-to-leaf path such that the sum
        of node values along the path equals targetSum.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.
            targetSum (int): The target sum for the root-to-leaf path.

        Returns:
            bool: True if such a path exists, False otherwise.

        Example:
            Given the tree:
                5
               / \
              4   8
             /   / \
            11  13  4
           /  \      \
          7    2      1

            targetSum = 22
            There exists a path 5->4->11->2 with sum 22, so returns True.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

        LeetCode: Beats 100% of submissions
        """
        self.path_is_exist = False

        def dfs(node, current):
            if not node:
                return 0

            current = current + node.val

            if not node.left and not node.right:
                if current == targetSum:
                    self.path_is_exist = True
                return

            dfs(node.left, current)
            dfs(node.right, current)

        dfs(root, 0)

        return self.path_is_exist
