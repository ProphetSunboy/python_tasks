class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Given two 0-indexed integer permutations A and B of length n, computes
        their prefix common list C.

        The prefix common list C is defined as:
            - C[i] = the count of numbers that have appeared at or before index
            i in both A and B.

        Args:
            A (List[int]): The first permutation list.
            B (List[int]): The second permutation list.

        Returns:
            List[int]: The prefix common list of A and B.

        Example:
            Input: A = [1,3,2,4], B = [3,1,2,4]
            Output: [0,2,3,4]

        Time Complexity: O(n), where n is the length of A and B.
        Space Complexity: O(n), for tracking the seen numbers.

        LeetCode: Beats 94.37% of submissions
        """
        seen_a = set()
        seen_b = set()

        res = []
        common = 0
        for i, (num_a, num_b) in enumerate(zip(A, B)):
            seen_a.add(num_a)
            seen_b.add(num_b)

            if num_a == num_b:
                common += 1
            else:
                if num_a in seen_b:
                    common += 1
                if num_b in seen_a:
                    common += 1

            res.append(common)

        return res
