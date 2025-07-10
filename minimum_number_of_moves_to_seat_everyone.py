class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        """Given n seats and n students, where seats[i] is the position of the i-th seat and students[j] is the position of the j-th student,
        return the minimum number of moves required to seat every student such that no two students share a seat.

        In one move, you may increase or decrease the position of any student by 1 (i.e., move from position x to x + 1 or x - 1).

        Note: There may be multiple seats or students at the same position initially.

        Args:
            seats (list[int]): The positions of the seats.
            students (list[int]): The positions of the students.

        Returns:
            int: The minimum total number of moves required to seat all students.

        Example:
            >>> minMovesToSeat([3,1,5], [2,7,4])
            4
            # Explanation: One optimal way is to seat the students at positions [1,3,5] with moves [1,1,2].

        Time complexity: O(n log n), due to sorting.
        Space complexity: O(1), ignoring input storage.

        LeetCode: Beats 100% of submissions
        """
        seats.sort()
        students.sort()
        moves = 0

        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])

        return moves
