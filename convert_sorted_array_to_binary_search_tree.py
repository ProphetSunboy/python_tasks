# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Converts a sorted integer list to a height-balanced binary search tree.

        Each subtree's height difference is at most one, ensuring balance.

        Args:
            nums (List[int]): Sorted list of integers (ascending order).

        Returns:
            Optional[TreeNode]: Root node of the constructed height-balanced BST.

        Example:
            Input: nums = [-10, -3, 0, 5, 9]
            Output: [0, -3, 9, -10, None, 5]

        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(h), where h is the height of the tree (recursion stack).

        LeetCode: Beats 100% of submissions
        """

        def helper(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)
