# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Determines if there exist two elements in the BST such that their sum equals k.

        Args:
            root (Optional[TreeNode]): The root node of the binary search tree.
            k (int): Target sum to find from two distinct nodes.

        Returns:
            bool: True if there exist two elements whose values sum to k, False otherwise.

        Example:
            Input: root = [5,3,6,2,4,None,7], k = 9
            Output: True
            Explanation: 5 + 4 = 9.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), for the hash set storing values of visited nodes.

        LeetCode: Beats 100% of submissions
        """
        self.seen = set()

        def traverse(node):
            if not node:
                return False

            if k - node.val in self.seen:
                return True

            self.seen.add(node.val)

            return traverse(node.left) or traverse(node.right)

        return traverse(root)
