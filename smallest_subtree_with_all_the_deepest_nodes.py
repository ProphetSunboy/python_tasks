# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, returns the smallest subtree containing
        all the deepest nodes.

        The depth of a node is defined as its shortest distance to the root.
        All nodes with the maximum depth are considered the deepest.
        The returned subtree is the minimal tree that contains all such deepest
        nodes.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            Optional[TreeNode]: The root node of the smallest subtree containing
            all the deepest nodes.

        Example:
            Input: root = [3,5,1,6,2,0,8,null,null,7,4]
            Output: [2,7,4]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to recursion).

        LeetCode: Beats 100% of submissions
        """

        def traverse(node, depth):
            if not node.left and not node.right:
                return [node, depth]

            left_depth = [0, -1]
            right_depth = [0, -1]
            if node.left:
                left_depth = traverse(node.left, depth + 1)
            if node.right:
                right_depth = traverse(node.right, depth + 1)

            if left_depth[1] == right_depth[1]:
                return [node, left_depth[1]]
            elif left_depth[1] > right_depth[1]:
                return left_depth

            return right_depth

        return traverse(root, 0)[0]
