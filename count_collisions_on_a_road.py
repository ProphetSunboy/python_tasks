class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        Given a string directions representing the movement of n cars on a road,
        compute the total number of collisions that will occur.

        Each character in directions represents a car:
            'L' - moves left
            'R' - moves right
            'S' - stays stationary

        Collisions rules:
        - Two cars moving in opposite directions that collide result in 2 collisions.
        - A moving car colliding with a stationary car results in 1 collision.
        - After a collision, involved cars become stationary.

        Args:
            directions (str): String of length n, with each character in
            {'L', 'R', 'S'}, representing car movements.

        Returns:
            int: Total number of collisions that will occur.

        Example:
            Input: directions = "RLRSLL"
            Output: 5

        Time Complexity: O(N), where N is the number of cars.
        Space Complexity: O(1).
        """
        collisions = 0
        i = 0
        lefts = 0

        while i < len(directions):
            if directions[i] == "R":
                if i < len(directions) - 1:
                    if directions[i + 1] == "L":
                        collisions += 2
                        i += 2
                    elif directions[i + 1] == "S":
                        collisions += 1
                        i += 2
                    else:
                        j = i + 1
                        while j < len(directions) and directions[j] == "R":
                            j += 1

                        if j == len(directions):
                            i = j
                        else:
                            collisions += j - i
                            if directions[j] == "L":
                                collisions += 1

                            i = j + 1
                else:
                    i += 1
            elif directions[i] == "L":
                lefts += 1
                if lefts < i + 1:
                    collisions += 1

                i += 1
            else:
                i += 1

        return collisions
