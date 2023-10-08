class RecentCounter:
    """
    You have a RecentCounter class which counts the number of recent requests
    within a certain time frame.

    Implement the RecentCounter class:

        RecentCounter() Initializes the counter with zero recent requests.
        int ping(int t) Adds a new request at time t, where t represents some
        time in milliseconds, and returns the number of requests that has
        happened in the past 3000 milliseconds (including the new request).
        Specifically, return the number of requests that have happened in the
        inclusive range [t - 3000, t].

    It is guaranteed that every call to ping uses a strictly larger value of t
    than the previous call.

    LeetCode: Beats 95.21%
    """

    def __init__(self):
        self.requests = []
        self.i = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[self.i] < self.requests[-1] - 3000:
            self.i += 1

        return len(self.requests) - self.i
