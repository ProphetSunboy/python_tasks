# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """
        Determines whether a binary tree is uni-valued (all nodes have the same value).

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the binary tree is uni-valued, False otherwise.

        Example:
            Input: [1,1,1,1,1,None,1]
            Output: True
            Explanation: All nodes have the value 1.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree due to recursion stack.

        LeetCode: Beats 100% of submissions
        """
        if not root:
            return True

        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
