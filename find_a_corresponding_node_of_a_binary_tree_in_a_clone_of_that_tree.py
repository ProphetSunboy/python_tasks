# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        """
        Given two binary trees, `original` and `cloned`, and a reference to a node `target` in the original tree,
        returns the corresponding node in the cloned tree.

        The cloned tree is a deep copy of the original tree. You are not allowed
        to modify either tree or the target node.
        The answer must be a reference to a node in the cloned tree corresponding
        to `target` in the original tree.

        Args:
            original (TreeNode): The root node of the original binary tree.
            cloned (TreeNode): The root node of the cloned binary tree.
            target (TreeNode): A reference to a node in the original tree.

        Returns:
            TreeNode: The reference to the node in the cloned tree that corresponds
            to the target node in the original tree.

        Example:
            For the following trees:
                original = [7, 4, 3, None, None, 6, 19]
                cloned   = [7, 4, 3, None, None, 6, 19]
                target = reference to node with value 3 in original

            Calling getTargetCopy(original, cloned, target) will return the reference to the node with value 3 in the cloned tree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

        LeetCode: Beats 93.19% of submissions
        """
        if not original:
            return None

        if original is target:
            return cloned

        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result

        return self.getTargetCopy(original.right, cloned.right, target)
