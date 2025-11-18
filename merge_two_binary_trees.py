# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        Merges two binary trees into a new binary tree.

        Given two binary trees root1 and root2, this function creates a new tree where:
            - If two nodes overlap (exist at the same position in both trees),
            their values are summed and used for the new node.
            - If only one node exists at a position, that node is used directly
            in the new tree.

        The merging process starts from the root nodes of both trees.

        Args:
            root1 (Optional[TreeNode]): The root of the first binary tree.
            root2 (Optional[TreeNode]): The root of the second binary tree.

        Returns:
            Optional[TreeNode]: The root of the merged binary tree.

        Example:
            Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
            Output: [3,4,5,5,4,null,7]

        Time Complexity: O(n), where n is the total number of nodes in both trees (visiting each non-null node once).
        Space Complexity: O(n), due to the recursion stack in the worst case (for completely unbalanced trees).

        LeetCode: Beats 100% of submissions
        """
        if not root1 and not root2:
            return None

        if not root1:
            return root2
        if not root2:
            return root1

        merged_root = TreeNode(root1.val + root2.val)

        merged_root.left = self.mergeTrees(root1.left, root2.left)
        merged_root.right = self.mergeTrees(root1.right, root2.right)

        return merged_root
