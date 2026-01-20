# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Convert a Binary Search Tree (BST) to a Greater Tree.

        Each node's value is replaced by the sum of all values greater than or
        equal to it in the BST.

        A binary search tree is defined as:
            - The left subtree of a node contains only nodes with keys less than the node's key.
            - The right subtree of a node contains only nodes with keys greater than the node's key.
            - Both subtrees must also be binary search trees.

        Args:
            root (Optional[TreeNode]): Root node of the BST.

        Returns:
            Optional[TreeNode]: The root node of the transformed Greater Tree.

        Example:
            Input: root representing BST [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
            Output: Greater Tree [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (for the recursion stack).

        LeetCode: Beats 100% of submissions
        """

        def traverse(node, add):
            if not node:
                return 0

            right = traverse(node.right, add)
            node.val += add if right == 0 else right
            left = traverse(node.left, node.val)

            return left if left != 0 else node.val

        traverse(root, 0)

        return root
