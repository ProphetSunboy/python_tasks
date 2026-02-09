class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Given the root of a binary search tree, return a balanced binary search tree
        with the same node values. If there is more than one answer, return any of them.

        A binary search tree is balanced if the depth of the two subtrees of
        every node never differs by more than 1.

        Args:
            root (TreeNode): The root of the input binary search tree.

        Returns:
            TreeNode: The root of the balanced binary search tree.

        Example:
            Input: root = [1,null,2,null,3,null,4,null,null]
            Output: [2,1,3,null,null,null,4]

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), to store the node values during in-order traversal.

        LeetCode: Beats 90.19% of submissions
        """
        vals = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            vals.append(node.val)
            in_order(node.right)

        in_order(root)

        def build_balanced_tree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(vals[mid])

            node.left = build_balanced_tree(left, mid - 1)
            node.right = build_balanced_tree(mid + 1, right)

            return node

        return build_balanced_tree(0, len(vals) - 1)
