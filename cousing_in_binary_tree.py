# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        Determines whether two nodes in a binary tree are cousins.

        Given the root of a binary tree with unique values and two distinct node values x and y,
        returns True if the nodes corresponding to x and y in the tree are cousins, and False otherwise.

        Two nodes are cousins if they are at the same depth but have different parents.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.
            x (int): The value of the first node.
            y (int): The value of the second node.

        Returns:
            bool: True if the nodes with values x and y are cousins, False otherwise.

        Example:
            Input:
                root = [1,2,3,4]
                x = 4
                y = 3
            Output: False

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), for the recursion stack and value tracking.

        LeetCode: Beats 100% of submissions
        """
        self.values = {}

        def traverse(node, curr):
            if not node:
                return False

            if node.left and node.right:
                if (node.left.val == x or node.left.val == y) and (
                    node.right.val == x or node.right.val == y
                ):
                    return False

            if node.val == x or node.val == y:
                if self.values.get(x, -1) == curr or self.values.get(y, -1) == curr:
                    return True

            self.values[node.val] = curr
            curr += 1

            return traverse(node.left, curr) or traverse(node.right, curr)

        return traverse(root, 0)
