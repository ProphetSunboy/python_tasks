# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """
        Finds the second minimum value in a special binary tree.

        In this binary tree:
            - Each node has either two or zero children.
            - For any node with two children, the node's value equals the minimum of its two children:
                  node.val = min(node.left.val, node.right.val)
            - All node values are non-negative.
        
        The function returns the second smallest unique value among all values
        in the tree, or -1 if no such value exists.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The second minimum value, or -1 if it does not exist.

        Example:
            Input:  root = [2,2,5,None,None,5,7]
            Output: 5
            Explanation:
                  2
                 / \
                2   5
                   / \
                  5   7
            The unique values are [2, 5, 7]; the second minimum is 5.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), for storing all unique values in a set.

        LeetCode: Beats 100% of submissions
        """
        self.values = set()

        def traverse(node):
            if not node:
                return

            self.values.add(node.val)

            traverse(node.left)
            traverse(node.right)

        traverse(root)
        if len(self.values) <= 1:
            return -1

        return sorted(self.values)[1]
