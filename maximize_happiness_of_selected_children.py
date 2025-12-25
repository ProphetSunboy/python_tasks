class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
        Calculates the maximum possible sum of happiness values for selecting k
        children from a list, under the following conditions:

        - There are n children, each with an initial happiness value given in
        the list `happiness`.
        - In each of k turns, select one unselected child.
        - After each turn, happiness of all unselected children decreases by 1
        (but not below 0).

        Args:
            happiness (List[int]): List of initial happiness values for each
            child.
            k (int): Number of children to select.

        Returns:
            int: The maximum total happiness value achievable by selecting k
            children optimally.

        Example:
            Input: happiness = [6, 3, 8, 5], k = 2
            Output: 13
            Explanation: Select 8 (turn 1), remaining: [6, 3, 5] -> [5, 2, 4]
                         Then select 5 (now adjusted to 5), total = 8 + 5 = 13

        Time Complexity: O(n log n), due to sorting.
        Space Complexity: O(1), ignoring input storage.

        LeetCode: Beats 95.74% of submissions
        """
        happiness.sort(reverse=True)
        max_happiness = 0

        for i in range(k):
            curr_happiness = happiness[i] - i
            if curr_happiness <= 0:
                break

            max_happiness += curr_happiness

        return max_happiness
