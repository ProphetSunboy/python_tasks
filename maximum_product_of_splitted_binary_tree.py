class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, split the tree into two by removing
        one edge such that the product of the sums of the two resulting subtrees
        is maximized.

        Returns the maximum possible product of these sums modulo 10^9 + 7.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum product of sums of the two subtrees,
            modulo 10^9 + 7.

        Example:
            Input: root = [1,2,3,4,5,6]
            Output: 110

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), for storing sums of all subtrees.

        LeetCode: Beats 96.58% of submissions
        """
        all_sums = []

        def get_sum(node):
            if not node:
                return 0

            current_sum = node.val + get_sum(node.left) + get_sum(node.right)

            all_sums.append(current_sum)
            return current_sum

        total_sum = get_sum(root)

        max_prod = 0
        for s in all_sums:
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product

        return max_prod % (10**9 + 7)
