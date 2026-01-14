class Solution:
    def minOperations(self, boxes: str):
        """
        Given a binary string boxes of length n, where boxes[i] is '1' if the
        ith box contains a ball and '0' otherwise.

        In one operation, you can move one ball from a box to an adjacent box
        (i.e., from box i to box i-1 or box i+1).
        Your task is to return a list answer of size n such that answer[i] is
        the minimum number of operations required to move all the balls to the
        ith box.
        Note that you must consider the initial positions of the balls,
        and balls can be stacked in a box.

        Args:
            boxes (str): A binary string representing the initial configuration
            of balls in boxes.

        Returns:
            List[int]: List where the ith element is the minimum number of
            operations needed to move all balls to the ith box.

        Example:
            Input: boxes = "110"
            Output: [1,1,3]

        Time Complexity: O(n), where n is the length of boxes.
        Space Complexity: O(n), for the result list.

        LeetCode: Beats 90.49% of submissions
        """
        n = len(boxes)
        res = [0] * n

        count = 0
        pos_sum = 0
        for i in range(n):
            res[i] += count * i - pos_sum
            if boxes[i] == "1":
                count += 1
                pos_sum += i

        count = 0
        pos_sum = 0
        for i in range(n - 1, -1, -1):
            res[i] += pos_sum - count * i
            if boxes[i] == "1":
                count += 1
                pos_sum += i

        return res
