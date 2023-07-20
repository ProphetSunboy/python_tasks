class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        We are given an array asteroids of integers representing asteroids
        in a row.

        For each asteroid, the absolute value represents its size, and the sign
        represents its direction (positive meaning right,negative meaning left).
        Each asteroid moves at the same speed.

        Find out the state of the asteroids after all collisions.
        If two asteroids meet, the smaller one will explode. If both are the
        same size, both will explode. Two asteroids moving in the same
        direction will never meet.

        LeetCode: Beats 93.74%
        """
        left_a, right_a = [], 0
        res = []

        for a in asteroids:
            if a > 0:
                left_a.append(a)

            else:
                right_a = a

                # If there are no asteroids moving to the right, then just add it to result.
                if not left_a:
                    res.append(right_a)
                else:
                    while left_a and right_a != 0:
                        if left_a[-1] > -1 * right_a:
                            right_a = 0
                        elif left_a[-1] < -1 * right_a:
                            left_a.pop()
                        else:
                            left_a.pop()
                            right_a = 0
                            
                    # If asteroid moving to the left is heavier than all
                    # asteroids moving to the right, add right_a to result.        
                    if right_a != 0:
                        res.append(right_a)

        return res + left_a