class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Determines the number of students unable to eat lunch based on their sandwich preferences.

        The cafeteria offers two types of sandwiches: circular (0) and square (1).
        Each student in the queue has a preference for one type. At each step,
        if the student at the front of the queue prefers the sandwich on top of the stack,
        they take it and leave the queue; otherwise, they move to the end of the queue.
        This process continues until no student in the queue wants the sandwich on top.

        Args:
            students (List[int]): The preferences of each student in the queue (0 for circular, 1 for square).
            sandwiches (List[int]): The types of sandwiches in the stack (0 is the top of the stack).

        Returns:
            int: The number of students unable to eat.

        Example:
            >>> countStudents([1, 1, 0, 0], [0, 1, 0, 1])
            0

        Time Complexity: O(n), where n is the number of students.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        unable = 0
        sandwiches = sandwiches[::-1]
        students = deque(students)

        while unable < len(students):
            curr = students.popleft()

            if curr != sandwiches[-1]:
                unable += 1
                students.append(curr)
            else:
                unable = 0
                sandwiches.pop()

        return unable
