# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Determines whether a binary tree is symmetric around its center.

        This function checks if the tree is a mirror of itself, i.e., the left and right
        subtrees are mirror images.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the binary tree is symmetric, False otherwise.

        Example:
            Input:  root = [1,2,2,3,4,4,3]
            Output: True

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (recursion stack).

        LeetCode: Beats 100% of submissions
        """

        def isMirror(t1, t2):
            if not t1 and not t2:
                return True

            if not t1 or not t2:
                return False

            if t1.val != t2.val:
                return False

            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        if not root:
            return True

        return isMirror(root.left, root.right)
