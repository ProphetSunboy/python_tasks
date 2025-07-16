class Solution:
    def get_ball_digit_sum(self, ball: int) -> int:
        """Calculates the sum of the digits of a given integer.

        Args:
            ball (int): The integer whose digits will be summed.

        Returns:
            int: The sum of the digits of the input integer.

        Example:
            >>> get_ball_digit_sum(123)
            6
            >>> get_ball_digit_sum(405)
            9
        """
        digit_sum = 0

        while ball > 0:
            digit_sum += ball % 10
            ball //= 10

        return digit_sum

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """Returns the maximum number of balls in any box, where each ball numbered from lowLimit to highLimit (inclusive)
        is placed in a box whose number is the sum of the digits of the ball's number.

        Args:
            lowLimit (int): The starting number of the balls (inclusive).
            highLimit (int): The ending number of the balls (inclusive).

        Returns:
            int: The maximum number of balls in any box.

        Example:
            >>> countBalls(1, 10)
            2
            >>> countBalls(5, 15)
            2

        Time complexity: O(n * d), where n is highLimit - lowLimit + 1 and d is the number of digits in the largest ball number.
        Space complexity: O(k), where k is the number of possible digit sums (boxes).
        """
        boxes = dict()

        for ball in range(lowLimit, highLimit + 1):
            digit_sum = self.get_ball_digit_sum(ball)

            boxes[digit_sum] = boxes.get(digit_sum, 0) + 1

        return max(boxes.values())
