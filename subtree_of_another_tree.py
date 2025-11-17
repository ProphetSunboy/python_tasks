class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determines if one binary tree is a subtree of another.

        Given the roots of two binary trees, root and subRoot, returns True if
        subRoot is a subtree of root, i.e., if there exists a node in root such
        that the subtree rooted at that node is structurally identical to subRoot
        with the same node values.

        A subtree is defined as a node in the binary tree and all of its descendants.
        The whole tree itself can also be considered a subtree.

        Args:
            root (Optional[TreeNode]): Root of the main binary tree.
            subRoot (Optional[TreeNode]): Root of the subtree to check for.

        Returns:
            bool: True if subRoot is a subtree of root, False otherwise.

        Example:
            Given:
                root:
                     3
                    / \
                   4   5
                  / \
                 1   2

                subRoot:
                   4 
                  / \
                 1   2

            Output: True

            Explanation:
                The subtree rooted at the left child of root (node 4) is identical to subRoot.

        Time Complexity: O(N * M), where N is the number of nodes in root and M is the number of nodes in subRoot.
        Space Complexity: O(H), where H is the height of the tree (for recursion stack).
        """

        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (
                node1.val == node2.val
                and isSameTree(node1.left, node2.left)
                and isSameTree(node1.right, node2.right)
            )

        def traverse(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            return traverse(node.left) or traverse(node.right)

        return traverse(root)
