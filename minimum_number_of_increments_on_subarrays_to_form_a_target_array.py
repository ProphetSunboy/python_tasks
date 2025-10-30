class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Given an integer list target, where you start with a list 'initial' of the same length initialized with zeros.

        In each operation, you may select any sublist of initial and increment every element of the sublist by 1.

        Return the minimum number of operations required to transform initial into target.

        Args:
            target (List[int]): The desired target list.

        Returns:
            int: The minimum number of operations needed to form the target list from initial.

        Example:
            >>> minNumberOperations([1,2,3,2,1])
            3
            >>> minNumberOperations([3,1,1,2])
            4

        Time Complexity: O(n), where n is the length of target.
        Space Complexity: O(1)
        """
        operations = 0

        operations += target[0]

        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]

        return operations
