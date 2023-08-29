class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        You are given the customer visit log of a shop represented by a
        0-indexed string customers consisting only of characters 'N' and 'Y':

            if the ith character is 'Y', it means that customers come
            at the ith hour
            whereas 'N' indicates that no customers come at the ith hour.

        If the shop closes at the jth hour (0 <= j <= n), the penalty is
        calculated as follows:

            For every hour when the shop is open and no customers come, the
            penalty increases by 1.
            For every hour when the shop is closed and customers come, the
            penalty increases by 1.

        Return the earliest hour at which the shop must be closed to incur a
        minimum penalty.

        Note that if a shop closes at the jth hour, it means the shop is closed
        at the hour j.

        :param str customers: 0-indexed string consisting only of characters 'N'
        and 'Y'
        :returns int closing_hour: the earliest hour at which the shop must be
        closed to incur a minimum penalty

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 98.49%
        """
        min_penalty = customers.count("Y")
        closing_hour = 0

        curr_penalty = min_penalty
        for i, customer in enumerate(customers):
            if customer == "N":
                curr_penalty += 1
            else:
                curr_penalty -= 1

                if curr_penalty < min_penalty:
                    min_penalty = curr_penalty
                    closing_hour = i + 1

        return closing_hour
