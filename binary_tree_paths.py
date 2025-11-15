# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Returns all root-to-leaf paths in a binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[str]: A list of strings, each representing a path from root to leaf.
                Each path is formatted as a sequence of node values separated by '->'.

        Example:
            Input:  root = [1,2,3,None,5]
            Output: ["1->2->5","1->3"]

            Explanation:
                1
               / \
              2   3
               \
                5
            The paths are: "1->2->5", "1->3"

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the maximum height of the tree (recursion stack).

        LeetCode: Beats 100% of submissions
        """
        self.paths = []

        def traverse(node, curr_path):
            if not node:
                return

            if not node.left and not node.right:
                self.paths.append(curr_path)

            curr_path.append(str(node.val))

            traverse(node.left, curr_path[:])
            traverse(node.right, curr_path[:])

        traverse(root, [])

        return ["->".join(path) for path in self.paths]
