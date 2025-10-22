class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: list[int],
        experience: list[int],
    ) -> int:
        """
        Calculate the minimum number of training hours needed to win a competition.

        You start with initial amounts of energy and experience. There are n opponents,
        each with specified energy and experience values. To defeat an opponent, you must
        have strictly greater energy and experience than them. After defeating an opponent,
        your energy decreases by the opponent's energy, and your experience increases by the
        opponent's experience.

        Before the competition, you can train for any number of hours. Each hour of training
        increases either your energy or experience by 1.

        Args:
            initialEnergy (int): Your starting energy level.
            initialExperience (int): Your starting experience level.
            energy (List[int]): List of opponents energy requirements.
            experience (List[int]): List of opponents experience levels.

        Returns:
            int: The minimum hours of training required to defeat all opponents.

        Example:
            >>> minNumberOfHours(1, 1, [1, 1, 1, 1], [1, 1, 1, 50])
            51

        Time Complexity: O(n), where n is the number of opponents.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        training_hours = max(0, sum(energy) - initialEnergy + 1)
        curr_exp = initialExperience

        for exp in experience:
            if curr_exp > exp:
                curr_exp += exp
            else:
                training_hours += exp - curr_exp + 1
                curr_exp += exp

        return training_hours
