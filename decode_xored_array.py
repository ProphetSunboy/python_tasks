class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        Decodes the original list from its encoded form.

        Given an encoded list where encoded[i] = arr[i] XOR arr[i + 1] and the first element of the original list,
        reconstructs and returns the original list.

        Args:
            encoded (List[int]): The encoded list of length n - 1.
            first (int): The first element of the original list.

        Returns:
            List[int]: The decoded original list.

        Example:
            >>> decode([1,2,3], 1)
            [1, 0, 2, 1]

        Time Complexity: O(n), where n is the length of the decoded list.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        arr = [first]

        for num in encoded:
            arr.append(num ^ arr[-1])

        return arr
