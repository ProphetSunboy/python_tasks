from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List


class Router:
    """
    Router: A data structure to efficiently manage data packets in a network router.

    Each data packet has:
        - source: Unique identifier for the sender.
        - destination: Unique identifier for the receiver.
        - timestamp: Arrival time at the router.

    Methods:
        __init__(memoryLimit: int)
            Initializes the router with a fixed memory limit (maximum number of packets stored).
            If adding a new packet exceeds this limit, the oldest packet is removed.

        addPacket(source: int, destination: int, timestamp: int) -> bool
            Adds a packet to the router.
            Returns True if the packet is added (not a duplicate), False otherwise.
            A duplicate is a packet with the same source, destination, and timestamp already present.

        forwardPacket() -> List[int]
            Forwards (removes and returns) the next packet in FIFO order.
            Returns [source, destination, timestamp] of the forwarded packet.
            Returns an empty list if no packets are available.

        getCount(destination: int, startTime: int, endTime: int) -> int
            Returns the number of packets currently stored with the specified destination and
            timestamps in the inclusive range [startTime, endTime].

    Notes:
        - addPacket is always called with non-decreasing timestamps.
        - All operations are designed for efficiency in a high-throughput network environment.

    LeetCode: Beats 98.23% of submissionss
    """

    def __init__(self, memoryLimit: int):
        self.storage = deque()
        self.memory_lim = memoryLimit
        self.seen = set()
        self.index = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.seen:
            return False

        if len(self.storage) == self.memory_lim:
            old_packet = self.storage.popleft()
            self.seen.remove(old_packet)
            old_dest = old_packet[1]
            old_time = old_packet[2]

            idx_list = self.index[old_dest]
            i = bisect_left(idx_list, old_time)
            if i < len(idx_list) and idx_list[i] == old_time:
                idx_list.pop(i)

        self.storage.append(packet)
        self.seen.add(packet)

        insert_list = self.index[destination]
        insert_pos = bisect_right(insert_list, timestamp)
        insert_list.insert(insert_pos, timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.storage:
            return []

        packet = self.storage.popleft()
        self.seen.remove(packet)

        dest = packet[1]
        time = packet[2]
        idx_list = self.index[dest]
        i = bisect_left(idx_list, time)
        if i < len(idx_list) and idx_list[i] == time:
            idx_list.pop(i)

        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.index[destination]
        left = bisect_left(times, startTime)
        right = bisect_right(times, endTime)
        return right - left
