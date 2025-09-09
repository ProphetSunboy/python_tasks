class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        Simulates the spread and forgetting of a secret over n days.

        On day 1, one person discovers a secret. Each person will start sharing
        the secret with a new person every day, beginning delay days after discovering it.
        Each person forgets the secret forget days after discovering it and cannot
        share it on or after the day they forget.

        Args:
            n (int): The total number of days.
            delay (int): The number of days after which a person starts sharing the secret.
            forget (int): The number of days after which a person forgets the secret.

        Returns:
            int: The number of people who know the secret at the end of day n, modulo 10^9 + 7.

        Example:
            >>> peopleAwareOfSecret(6, 2, 4)
            5

        Time Complexity: O(n * forget)
        Space Complexity: O(forget)
        """
        people = [0] * forget
        people[-1] = 1

        for i in range(1, n):
            share_secret = 0
            for j in range(len(people) - 1):
                people[j] = people[j + 1]
                if j < forget - delay:
                    share_secret += people[j]

            people[-1] = share_secret

        return sum(people) % (10**9 + 7)
