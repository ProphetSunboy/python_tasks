# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Calculates the sum of all node values in a binary search tree (BST) that
        fall within a given inclusive range [low, high].

        Args:
            root (Optional[TreeNode]): The root node of the binary search tree.
            low (int): The lower bound of the range (inclusive).
            high (int): The upper bound of the range (inclusive).

        Returns:
            int: The sum of values of all nodes with a value in the range [low, high].

        Example:
            Given the following BST:
                10
               /  \
              5   15
             / \    \
            3   7   18
            rangeSumBST(root, 7, 15) returns 32 (7 + 10 + 15)

        Time Complexity: O(n), where n is the number of nodes in the tree (in the worst case, all nodes are visited).
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

        LeetCode: Beats 100% of submissions
        """
        if not root:
            return 0

        curr = 0
        if low <= root.val <= high:
            curr = root.val

        if root.val > high:
            return curr + self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            return curr + self.rangeSumBST(root.right, low, high)

        return (
            curr
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
