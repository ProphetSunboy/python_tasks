# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        Evaluates a full boolean binary tree where:
            - Each leaf node has a value of 0 or 1 (False or True).
            - Non-leaf nodes have a value of 2 (OR) or 3 (AND),
              representing boolean operations to apply to their two child nodes.

        The function recursively evaluates the tree as follows:
            - If the node is a leaf, return True if its value is 1, otherwise False.
            - If the node is non-leaf, evaluate the left and right children,
              then apply the logical operation corresponding to its value (OR or AND) 
              to the child evaluations.

        Args:
            root (Optional[TreeNode]): The root of the full binary tree to evaluate.

        Returns:
            bool: The result of evaluating the Boolean binary tree.

        Example:
            Tree with structure:
                2
               / \
              1   3
                 / \
                0   1

            Represents: 1 OR (0 AND 1) -> 1 OR 0 -> True

        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(h), where h is the height of the tree (for recursion stack).

        LeetCode: Beats 100% of submissions
        """
        if not root.left and not root.right:
            return bool(root.val)

        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        if root.val == 2:
            return left_val or right_val
        elif root.val == 3:
            return left_val and right_val
