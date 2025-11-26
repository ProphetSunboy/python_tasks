# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the sum of the values of the deepest leaves in a binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The sum of the values of the deepest leaves.

        Example:
            Input:
                root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
            Output:
                15
            Explanation:
                The deepest leaves are nodes with values 7 and 8 (depth 3), their sum is 15.

        Time Complexity: O(N), where N is the number of nodes in the tree.
        Space Complexity: O(H), where H is the height of the tree (for recursion stack).
        """
        self.deepest_sum = 0
        self.deepest = 0

        def traverse(node, curr):
            if not node:
                return

            if not node.left and not node.right:
                if curr > self.deepest:
                    self.deepest_sum = node.val
                    self.deepest = curr
                elif curr == self.deepest:
                    self.deepest_sum += node.val

            traverse(node.left, curr + 1)
            traverse(node.right, curr + 1)

        traverse(root, 0)

        return self.deepest_sum
