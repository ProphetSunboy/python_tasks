class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """
        Given two positive integer lists spells and potions, where spells[i] is
        the strength of the ith spell and potions[j] is the strength of the jth potion,
        and an integer success, determine for each spell how many potions can
        form a successful pair with it.

        A pair (spell, potion) is successful if spell * potion >= success.

        Args:
            spells (List[int]): List of spell strengths.
            potions (List[int]): List of potion strengths.
            success (int): The minimum required product for a successful pair.

        Returns:
            List[int]: For each spell, the number of potions that form a successful pair.

        Example:
            >>> successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)
            [4, 0, 3]

        Time Complexity: O(n log m), where n is the length of spells and m is the length of potions (due to sorting and binary search).
        Space Complexity: O(n + m), for the output and auxiliary data structures.

        LeetCode: Beats 98.39% of submissions
        """
        potions.sort(reverse=True)
        spells_s = sorted(set(spells), reverse=True)
        pairs = []
        seen_spells = {}

        for spell in spells_s:
            if spell in seen_spells:
                continue

            successful = 0
            i = len(potions) - 1
            while 0 <= i < len(potions):
                if spell * potions[i] < success:
                    potions.pop()
                else:
                    successful += i + 1
                    break

                i -= 1

            seen_spells[spell] = successful

        for spell in spells:
            pairs.append(seen_spells[spell])

        return pairs
