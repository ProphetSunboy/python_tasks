# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Search for a node with a given value in a binary search tree (BST) and return 
        the subtree rooted at that node. If no node with the specified value exists, return None.

        Args:
            root (Optional[TreeNode]): The root node of the BST.
            val (int): The value to search for.

        Returns:
            Optional[TreeNode]: The node whose value equals 'val' and its subtree,
            or None if not found.

        Example:
            Given the tree:
                4
               / \
              2   7
             / \
            1   3

            searchBST(root, 2) returns the subtree:
                2
               / \
              1   3

            searchBST(root, 5) returns None.

        Time Complexity: O(n), where n is the number of nodes in the trees.
        Space Complexity: O(h), due to the recursion stack (h is the height of the tree).

        LeetCode: Beats 100% of submissions
        """

        def dfs(node):
            if not node:
                return

            if node.val == val:
                return node

            node_left = dfs(node.left)

            if node_left:
                return node_left

            node_right = dfs(node.right)

            return node_right

        return dfs(root)
