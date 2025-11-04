"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        """
        Given the root of an n-ary tree, returns the postorder traversal of its nodes' values.

        In postorder traversal, children are visited before their parent node.
        That is, for each node, traverse all its children first (left to right),
        then visit the node itself.

        Args:
            root (Node): The root of the n-ary tree.

        Returns:
            List[int]: The list of node values in postorder traversal order.

        Example:
            Given the following N-ary Tree:
                    1
                  / | \
                 3  2  4
                / \
               5   6

            postorder(root) -> [5,6,3,2,4,1]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), due to the recursion stack and result list.

        LeetCode: Beats 94.09% of submissions
        """
        result = []

        def dfs(node):
            if not node:
                return

            for child in node.children:
                dfs(child)

            result.append(node.val)

        dfs(root)
        return result
