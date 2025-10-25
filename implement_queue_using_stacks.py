class MyQueue:
    """
    MyQueue implements a First-In-First-Out (FIFO) queue using only two stacks.

    Methods:
        - push(x): Add element x to the end of the queue.
        - pop(): Remove and return the element from the front of the queue.
        - peek(): Get the front element of the queue without removing it.
        - empty(): Return True if the queue is empty, False otherwise.

    Notes:
        - Only standard stack operations are allowed: push to top, pop/peek from top, check size or empty.
        - Stacks can be simulated using native list or deque structures as long as only stack operations are used.

    Time Complexity:
        - Amortized O(1) per operation.

    Space Complexity:
        - O(n), where n is the number of elements in the queue.

    LeetCode: Beats 100% of submissions
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return val

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1) == 0
