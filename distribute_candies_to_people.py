class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        """
        We distribute some number of candies, to a row of n = num_people people
        in the following way:

        We then give 1 candy to the first person, 2 candies to the second
        person, and so on until we give n candies to the last person.

        Then, we go back to the start of the row, giving n + 1 candies to the
        first person, n + 2 candies to the second person, and so on until we
        give 2 * n candies to the last person.

        This process repeats (with us giving one more candy each time, and
        moving to the start of the row after we reach the end) until we run out
        of candies. The last person will receive all of our remaining candies
        (not necessarily one more than the previous gift).

        Return a list (of length num_people and sum candies) that represents
        the final distribution of candies.

        :param int candies: integer number of candies
        :param int num_people: number of people to distribute candies
        :returns list[int] distr: final distribution of candies

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.39%
        """
        distr = [0] * num_people
        curr_gift = 1
        i = 0

        while candies >= curr_gift:
            distr[i % num_people] += curr_gift
            candies -= curr_gift
            curr_gift += 1
            i += 1

        if candies != 0:
            distr[i % num_people] += candies

        return distr
