class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Rearranges the given binary search tree into an increasing order search tree.

        Given the root of a binary search tree (BST), rearrange the tree so that
        it becomes a "right-skewed" tree: 
        - The leftmost node in the BST becomes the new root.
        - Every node has no left child and only one right child, ordered
        according to the in-order traversal of the BST.

        Args:
            root (Optional[TreeNode]): The root of the binary search tree.

        Returns:
            Optional[TreeNode]: The new root of the rearranged increasing order search tree.

        Example:
            Input:
                5
               / \
              3   6
             / \   \
            2   4   8
           /       / \
          1       7   9

            Output:
            1
             \
              2
               \
                3
                 \
                  4
                   \
                    5
                     \
                      6
                       \
                        7
                         \
                          8
                           \
                            9

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), due to the storage of the node sequence during traversal.

        LeetCode: Beats 100% of submissions
        """

        def inorder(node):
            if not node:
                return []

            return inorder(node.left) + [node] + inorder(node.right)

        nodes = inorder(root)

        dummy = TreeNode(0)
        current = dummy

        for node in nodes:
            node.left = None
            current.right = node
            current = current.right

        return dummy.right
