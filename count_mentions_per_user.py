class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        """
        Counts the total number of mentions per user based on a list of events.

        Args:
            numberOfUsers (int): Total number of users (indexed from 0 to numberOfUsers-1).
            events (List[List[str]]): List of events, where each event is of form:
                - ["MESSAGE", timestamp, mentions_string]: A message mentioning users at given timestamp.
                  mentions_string can include:
                    - "id<number>" (e.g., "id5"): mentions user with index <number>;
                    multiple IDs may be space-separated; duplicates are allowed
                    and each mention counts.
                    - "ALL": mentions all users.
                    - "HERE": mentions all users who are currently online.
                - ["OFFLINE", timestamp, id]: The user with id goes offline at
                the given timestamp for 60 time units, and will automatically be
                online again at (timestamp + 60).

        Returns:
            List[int]: A list where element at index i is the total number of
            mentions received by user i in all MESSAGE events.

        Example:
            Input:
                numberOfUsers = 3
                events = [
                    ["MESSAGE", "1", "id0 id1"],
                    ["OFFLINE", "2", "1"],
                    ["MESSAGE", "3", "HERE"],
                    ["MESSAGE", "4", "ALL"]
                ]
            Output: [3, 2, 2]

        Time Complexity: O(E * U), where E is the number of events and U is numberOfUsers.
        Space Complexity: O(U).

        LeetCode: Beats 95.47% of submissions
        """
        events.sort(key=lambda event: (-int(event[1]), event[0]), reverse=True)
        users_mention = [0] * numberOfUsers
        users_online = [0] * numberOfUsers

        for e in events:
            if e[0] == "MESSAGE":
                if e[2] == "ALL":
                    for i in range(len(users_mention)):
                        users_mention[i] += 1
                elif e[2] == "HERE":
                    e_timestamp = int(e[1])
                    for i in range(len(users_mention)):
                        if e_timestamp >= users_online[i]:
                            users_mention[i] += 1
                else:
                    for i in e[2].split():
                        users_mention[int(i[2:])] += 1
            else:
                users_online[int(e[2])] = int(e[1]) + 60

        return users_mention
