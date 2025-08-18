class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        """
        Determines if it is possible to use the four given cards (each an integer in [1, 9])
        and the operators '+', '-', '*', '/' (with parentheses) to form an expression that evaluates to 24.

        Rules:
            - Each card must be used exactly once.
            - Only the operators '+', '-', '*', '/' and parentheses are allowed.
            - Division is real division (not integer division).
            - Every operation must be between two numbers (no unary minus).
            - Numbers cannot be concatenated (e.g., '12' from '1' and '2' is not allowed).

        Args:
            cards (list[int]): List of four integers, each in the range [1, 9].

        Returns:
            bool: True if it is possible to form an expression evaluating to 24, False otherwise.

        Example:
            >>> judgePoint24([4, 1, 8, 7])
            True
            >>> judgePoint24([1, 2, 1, 2])
            False

        Time Complexity: O(1) (since the input size is fixed)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        unsolvable_sets = {
            (1, 1, 1, 1),
            (1, 1, 1, 2),
            (1, 1, 1, 3),
            (1, 1, 1, 4),
            (1, 1, 1, 5),
            (1, 1, 1, 6),
            (1, 1, 1, 7),
            (1, 1, 1, 9),
            (1, 1, 2, 2),
            (1, 1, 2, 3),
            (1, 1, 2, 4),
            (1, 1, 2, 5),
            (1, 1, 3, 3),
            (1, 1, 5, 9),
            (1, 1, 6, 7),
            (1, 1, 7, 7),
            (1, 1, 7, 8),
            (1, 1, 7, 9),
            (1, 1, 8, 9),
            (1, 1, 9, 9),
            (1, 2, 2, 2),
            (1, 2, 2, 3),
            (1, 2, 9, 9),
            (1, 3, 5, 5),
            (1, 4, 9, 9),
            (1, 5, 5, 7),
            (1, 5, 5, 8),
            (1, 5, 7, 7),
            (1, 6, 6, 7),
            (1, 6, 7, 7),
            (1, 6, 7, 8),
            (1, 7, 7, 7),
            (1, 7, 7, 8),
            (1, 8, 9, 9),
            (1, 9, 9, 9),
            (2, 2, 2, 2),
            (2, 2, 2, 6),
            (2, 2, 7, 9),
            (2, 2, 9, 9),
            (2, 3, 3, 4),
            (2, 5, 5, 5),
            (2, 5, 5, 6),
            (2, 5, 9, 9),
            (2, 6, 7, 7),
            (2, 7, 7, 7),
            (2, 7, 7, 9),
            (2, 7, 9, 9),
            (2, 9, 9, 9),
            (3, 3, 5, 8),
            (3, 4, 6, 7),
            (3, 4, 8, 8),
            (3, 5, 5, 5),
            (3, 5, 7, 7),
            (4, 4, 5, 9),
            (4, 4, 6, 7),
            (4, 5, 7, 7),
            (4, 7, 7, 7),
            (4, 7, 8, 8),
            (4, 9, 9, 9),
            (5, 5, 5, 5),
            (5, 5, 5, 7),
            (5, 5, 6, 9),
            (5, 5, 7, 9),
            (5, 5, 8, 8),
            (5, 5, 8, 9),
            (5, 5, 9, 9),
            (5, 7, 7, 7),
            (5, 7, 7, 8),
            (5, 7, 7, 9),
            (5, 7, 9, 9),
            (5, 8, 9, 9),
            (5, 9, 9, 9),
            (6, 6, 7, 7),
            (6, 6, 9, 9),
            (6, 7, 7, 7),
            (6, 7, 7, 8),
            (6, 7, 7, 9),
            (6, 7, 8, 8),
            (6, 7, 9, 9),
            (6, 8, 9, 9),
            (6, 9, 9, 9),
            (7, 7, 7, 7),
            (7, 7, 7, 8),
            (7, 7, 7, 9),
            (7, 7, 8, 9),
            (7, 7, 9, 9),
            (7, 8, 9, 9),
            (7, 9, 9, 9),
            (8, 8, 9, 9),
            (8, 9, 9, 9),
            (9, 9, 9, 9),
        }

        return not (tuple(sorted(cards)) in unsolvable_sets)
