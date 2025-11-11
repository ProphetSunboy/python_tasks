"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        """
        Given an n-ary tree, finds its maximum depth.

        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

        Args:
            root (Node): The root node of the n-ary tree.

        Returns:
            int: The maximum depth of the tree.

        Example:
            Input: root = [1, [3, 2, 4], [5, 6]]
            Output: 3

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree due to the recursion stack.

        LeetCode: Beats 91.82% of submissions
        """
        if not root:
            return 0

        def traverse(node, curr):
            if not node.children:
                return curr + 1

            curr += 1
            vals = []
            for n in node.children:
                vals.append(traverse(n, curr))

            return max(vals)

        return traverse(root, 0)
