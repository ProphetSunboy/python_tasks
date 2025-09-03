class Solution:
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        """
        Determines if any element in the given integer list `nums` has a prime frequency.

        The frequency of an element is the number of times it appears in the list.
        A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

        Args:
            nums (list[int]): The list of integers to check.

        Returns:
            bool: True if any element's frequency is a prime number, False otherwise.

        Example:
            >>> checkPrimeFrequency([1, 2, 2, 3, 3, 3])
            True  # 2 appears twice (prime), 3 appears three times (prime)

        Time Complexity: O(n * sqrt(f)), where n is the number of unique elements and f is the maximum frequency.
        Space Complexity: O(n), for storing the frequency count.

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)

        for freq in c.values():
            if freq == 1:
                continue
            if freq % 2 == 0 and freq > 2:
                continue
            else:
                prime = True
                for i in range(2, freq // 2 + 1):
                    if freq % i == 0:
                        prime = False
                        break

                if prime:
                    return True

        return False
