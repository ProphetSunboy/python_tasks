class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        Given a list of integers arr, this function counts the number of triplets (i, j, k)
        such that 0 <= i < j <= k < len(arr), and the xor of arr[i] to arr[j-1] equals
        the xor of arr[j] to arr[k].

        For triplet (i, j, k):
            Let a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
            Let b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
            We count the triplet if a == b.

        Args:
            arr (List[int]): The list of integers for which to count the triplets.

        Returns:
            int: The number of such triplets.

        Example:
            Input: arr = [2,3,1,6,7]
            Output: 4

        Time Complexity: O(n^3), where n is the length of arr.
        Space Complexity: O(1)
        """
        triplets = 0

        for i in range(len(arr)):
            a = arr[i]
            for j in range(i + 1, len(arr)):
                b = arr[j]
                for k in range(j + 1, len(arr)):
                    if a == b:
                        triplets += 1

                    b ^= arr[k]

                if a == b:
                    triplets += 1
                a ^= arr[j]

        return triplets
