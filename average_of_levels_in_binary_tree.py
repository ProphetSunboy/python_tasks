# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Computes the average value of the nodes on each level of a binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[float]: A list of floats, where each element is the average
            value of the nodes at that level.

        Example:
            Input:  root = [3,9,20,None,None,15,7]
            Output: [3.0, 14.5, 11.0]

            Explanation:
                3
               / \
              9  20
                /  \
               15   7
            The average for each level is: [3], [(9+20)/2], [(15+7)/2] = [3.0, 14.5, 11.0]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the maximum height of the tree (due to recursion stack).

        LeetCode: Beats 100% of submissions
        """
        self.level_values = []

        def traverse(node, curr):
            if not node:
                return

            if len(self.level_values) <= curr:
                self.level_values.append([1, node.val])
            else:
                self.level_values[curr][0] += 1
                self.level_values[curr][1] += node.val

            traverse(node.left, curr + 1)
            traverse(node.right, curr + 1)

        traverse(root, 0)
        res = []
        for count, val in self.level_values:
            res.append(val / count)

        return res
