class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """
        Given an n x n binary matrix image, flip the image horizontally, then
        invert it, and return the resulting image.

        To flip an image horizontally means that each row of the image is
        reversed.

        For example, flipping [1,1,0] horizontally results in [0,1,1].

        To invert an image means that each 0 is replaced by 1, and each 1 is
        replaced by 0.

        For example, inverting [0,1,1] results in [1,0,0].


        LeetCode: Beats 98.35%
        """
        res = [[0] * len(image[0]) for _ in range(len(image))]

        for i in range(len(image)):
            k = 0
            for j in range(len(image) - 1, -1, -1):
                res[i][k] = (image[i][j] + 1) % 2
                k += 1

        return res
