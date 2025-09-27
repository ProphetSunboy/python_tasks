class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Determines if there exists a pattern of length m in the list arr that repeats k or more times consecutively.

        A pattern is defined as a sublist (a consecutive sequence of elements)
        of length m that appears at least k times in a row without overlapping.

        Args:
            arr (List[int]): The input list of positive integers.
            m (int): The length of the pattern to search for.
            k (int): The minimum number of consecutive repetitions required.

        Returns:
            bool: True if such a pattern exists, False otherwise.

        Example:
            >>> containsPattern([1,2,1,2,1,1,1,3], 2, 2)
            True

        Time Complexity: O(N), where N is the length of arr.
        Space Complexity: O(N), due to storage of patterns.

        LeetCode: Beats 100% of submissions
        """
        for j in range(m):
            patterns = [tuple(arr[i : i + m]) for i in range(j, len(arr), m)]

            curr_pattern = patterns[0]
            curr_len = 1

            for p in range(1, len(patterns)):
                if patterns[p] == curr_pattern:
                    curr_len += 1

                    if curr_len >= k:
                        return True
                else:
                    curr_pattern = patterns[p]
                    curr_len = 1

        return False
