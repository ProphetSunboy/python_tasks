class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        """
        Calculates the total number of smooth descent periods in a stock price
        list.

        A smooth descent period is defined as one or more contiguous days such that,
        except for the first day, every day's price is exactly 1 less than the previous day's price.

        Args:
            prices (List[int]): List of integers representing daily stock prices.

        Returns:
            int: The total number of smooth descent periods.

        Example:
            Input: prices = [3, 2, 1, 4]
            Output: 7
            Explanation:
                Smooth descent periods:
                    - [3], [2], [1], [4]
                    - [3, 2], [2, 1], and [3, 2, 1]
                Total: 7

        Time Complexity: O(N), where N is the length of prices.
        Space Complexity: O(1).
        """
        smooth_descents = 0
        i = 1

        curr_descent = 1
        while i < len(prices):
            if prices[i - 1] - prices[i] == 1:
                curr_descent += 1
            else:
                smooth_descents += (curr_descent * (curr_descent + 1)) // 2
                curr_descent = 1

            i += 1

        smooth_descents += (curr_descent * (curr_descent + 1)) // 2

        return smooth_descents
