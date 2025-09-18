class TaskManager:
    """
    TaskManager is a system for managing user tasks, each with an associated priority.
    It supports efficient addition, modification, execution, and removal of tasks.

    Methods:
        __init__(tasks):
            Initializes the TaskManager with a list of tasks.
            Each task is represented as [userId, taskId, priority].

        add(userId, taskId, priority):
            Adds a new task with the specified taskId and priority for the given userId.
            Assumes taskId does not already exist.

        edit(taskId, newPriority):
            Updates the priority of the specified taskId to newPriority.
            Assumes taskId exists.

        rmv(taskId):
            Removes the task identified by taskId from the system.
            Assumes taskId exists.

        execTop():
            Executes and removes the task with the highest priority across all users.
            If multiple tasks share the highest priority, executes the one with the highest taskId.
            Returns the userId associated with the executed task.
            Returns -1 if no tasks are available.

    Notes:
        - A user may have multiple tasks.
        - Priorities are compared numerically; higher numbers indicate higher priority.
    """

    def __init__(self, tasks):
        self.tasks = {}
        self.heap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        self.tasks[taskId] = [userId, priority]
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, new_priority):
        if taskId in self.tasks:
            userId, _ = self.tasks[taskId]
            self.tasks[taskId] = [userId, new_priority]
            heapq.heappush(self.heap, (-new_priority, -taskId, taskId))

    def rmv(self, taskId):
        if taskId in self.tasks:
            del self.tasks[taskId]

    def execTop(self):
        while self.heap:
            neg_priority, neg_taskId, taskId = self.heap[0]
            if taskId in self.tasks:
                userId, priority = self.tasks[taskId]
                if priority == -neg_priority:
                    # Удаляем задачу из словаря и из кучи
                    del self.tasks[taskId]
                    heapq.heappop(self.heap)
                    return userId
            heapq.heappop(self.heap)
        return -1
