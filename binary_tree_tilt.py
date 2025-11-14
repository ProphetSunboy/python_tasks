# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the tilt of a binary tree.

        The tilt of a tree node is defined as the absolute difference between
        the sum of values in its left subtree and the sum of values in its right subtree.
        If a child is missing, its subtree sum is considered as 0.
        The tilt of the whole tree is the sum of all node tilts in the tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The total tilt of all nodes in the binary tree.

        Example:
            Input:  root = [1,2,3]
            Output: 1
        Explanation: 
                  1
                 / \
                2   3
            Tilt of node 2 : 0
            Tilt of node 3 : 0
            Tilt of node 1 : |2-3| = 1
            Total tilt = 1

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (recursion stack).

        LeetCode: Beats 100% of submissions
        """
        self.tilt = 0

        def traverse(node):
            if not node:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            self.tilt += abs(left - right)

            return node.val + left + right

        traverse(root)

        return self.tilt
