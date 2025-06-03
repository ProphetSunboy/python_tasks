class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        """Given a circular list code and a key k, decrypt the code by replacing each number according to k.

        Args:
            code (list[int]): Circular list of integers to decrypt
            k (int): Key determining how to replace numbers
                     If k > 0: replace with sum of next k numbers
                     If k < 0: replace with sum of previous k numbers
                     If k == 0: replace with 0

        Returns:
            list[int]: Decrypted list with replaced numbers

        Example:
            >>> decrypt([5,7,1,4], 3)
            [12,10,16,13]
            >>> decrypt([1,2,3,4], 0)
            [0,0,0,0]
            >>> decrypt([2,4,9,3], -2)
            [12,5,6,13]

        Time complexity: O(n*k) where n is length of code
        Space complexity: O(n) for storing decrypted list

        LeetCode: Beats 100% of submissions
        """
        decrypted_code = [0] * len(code)
        doubled_code = code + code

        if k > 0:
            for i in range(len(code)):
                decrypted_code[i] = sum(doubled_code[(i + 1) : (i + k + 1)])

        elif k < 0:
            for i in range(len(code)):
                decrypted_code[i] += sum(
                    doubled_code[len(code) + i + k : len(code) + i]
                )

        return decrypted_code
