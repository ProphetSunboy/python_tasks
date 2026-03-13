class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        """
        Calculate the minimum time required for workers to reduce the mountain
        height to zero.

        The workers operate simultaneously. For worker i:
            - To decrease the mountain's height by x units, the time taken is:
                workerTimes[i] + 2*workerTimes[i] + ... + x*workerTimes[i]

        For example:
            - Reducing the height by 1 unit takes workerTimes[i] seconds.
            - Reducing the height by 2 units takes
            workerTimes[i] + 2*workerTimes[i] seconds, and so on.

        Args:
            mountainHeight (int): The initial height of the mountain.
            workerTimes (List[int]): Work time in seconds for each worker.

        Returns:
            int: The minimum number of seconds required for the workers to make
            the mountain height 0.

        Example:
            Input: mountainHeight = 4, workerTimes = [2,1,1]
            Output: 3

        Time Complexity: O(n * log(max_possible_time)), where n is the number
                of workers.
        Space Complexity: O(1), only constant extra space is used.

        LeetCode: Beats 90.51% of submissions.
        """

        def can_finish(time_limit):
            total_height_reduced = 0
            for w in workerTimes:
                x = int((-1 + math.sqrt(1 + 8 * time_limit / w)) / 2)
                total_height_reduced += x
                if total_height_reduced >= mountainHeight:
                    return True
            return total_height_reduced >= mountainHeight

        low = 1
        min_w = min(workerTimes)
        high = min_w * mountainHeight * (mountainHeight + 1) // 2

        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_finish(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
