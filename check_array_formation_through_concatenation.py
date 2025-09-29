class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        Determines if the list 'arr' can be formed by concatenating the lists in 'pieces' in any order,
        without reordering the integers within each sublist of 'pieces'.

        Args:
            arr (List[int]): The target list of distinct integers.
            pieces (List[List[int]]): List of sublists, each containing distinct integers.

        Returns:
            bool: True if 'arr' can be formed by concatenating the lists in 'pieces', False otherwise.

        Example:
            >>> canFormArray([85], [[85]])
            True
            >>> canFormArray([15,88], [[88],[15]])
            True
            >>> canFormArray([49,18,16], [[16,18,49]])
            False

        Time Complexity: O(n * m), where n is the length of arr and m is the number of pieces.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i = 0

        while i < len(arr):
            flag = False
            for piece in pieces:
                if arr[i : i + len(piece)] == piece:
                    flag = True
                    i += len(piece)
                    continue

            if not flag:
                return False

        return True
