class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """Counts the number of good pairs (i, j) between two lists.

        A pair (i, j) is called "good" if `nums1[i]` is divisible by
        `nums2[j] * k`.

        Args:
            nums1 (list[int]): The first integer list.
            nums2 (list[int]): The second integer list.
            k (int): A positive integer multiplier.

        Returns:
            int: The total number of good pairs.

        Example:
            >>> numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1)
            5
            >>> numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3)
            2

        LeetCode: Beats 100% of submissions
        """
        good_pairs = 0
        sorted_nums2 = sorted(nums2)

        for i, num in enumerate(nums1):
            for j, n in enumerate(sorted_nums2):
                if n * k > num:
                    break

                if num % (n * k) == 0:
                    good_pairs += 1

        return good_pairs
