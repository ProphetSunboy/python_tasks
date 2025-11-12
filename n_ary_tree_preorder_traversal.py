"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        """
        Return the preorder traversal of an n-ary tree's node values.

        Args:
            root (Optional[Node]): The root node of the n-ary tree.

        Returns:
            List[int]: Preorder traversal of the values of the nodes.

        Example:
            Input: root = Node(1, [Node(3), Node(2), Node(4)])
            Output: [1, 3, 2, 4]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree due to recursion stack.

        LeetCode: Beats 97.05% of submissions
        """
        self.res = []

        def traverse(node):
            if not node:
                return

            self.res.append(node.val)
            for n in node.children:
                traverse(n)

        traverse(root)

        return self.res
