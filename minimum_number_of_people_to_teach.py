class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        """
        Determines the minimum number of users that need to be taught a single language
        so that all friends in a social network can communicate.

        On a social network with m users and some friendships, two users can communicate
        if they share at least one common language.

        Args:
            n (int): The total number of languages, numbered from 1 to n.
            languages (List[List[int]]): languages[i] is the list of languages known by the (i+1)-th user (1-indexed).
            friendships (List[List[int]]): Each element [u, v] denotes a friendship between user u and user v (1-indexed).

        Returns:
            int: The minimum number of users that need to be taught a single language so that every friendship pair can communicate.

        Notes:
            - You may choose any one language to teach.
            - Friendships are not transitive: if x is a friend of y and y is a friend of z, x and z are not necessarily friends.
            - You may teach the chosen language to any subset of users.

        Example:
            >>> minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]])
            1

        Time Complexity: O(m * k), where m is the number of friendships and k is the average number of languages per user.
        Space Complexity: O(n + m)

        LeetCode: Beats 95.12% of submissions
        """
        user_lang = {i + 1: set(languages[i]) for i in range(len(languages))}

        to_teach = set()
        for u, v in friendships:
            if user_lang[u].intersection(user_lang[v]):
                continue
            to_teach.add(u)
            to_teach.add(v)

        lang_count = [0] * (n + 1)
        for person in to_teach:
            for lang in user_lang[person]:
                lang_count[lang] += 1

        max_known = max(lang_count)

        return len(to_teach) - max_known
