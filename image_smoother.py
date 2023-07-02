class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """
        An image smoother is a filter of the size 3 x 3 that can be applied to
        each cell of an image by rounding down the average of the cell and the
        eight surrounding cells. If one or more of the surrounding cells of a
        cell is not present, we do not consider it in the average.
        Given an m x n integer matrix img representing the grayscale of an
        image, return the image after applying the smoother on each cell of it.

        LeetCode: Beats 99.44%
        """
        smoothed_img = []

        len_rows = len(img)
        len_cols = len(img[0])

        for i in range(len_rows):
            smoothed_img.append([0] * len_cols)

            for j in range(len_cols):
                k = 1
                summ = img[i][j]
                
                # If not in the corners we can sum up all values without checking.
                if (j >= 1 and i >= 1) and (i < len_rows-1 and j < len_cols-1):
                    summ += img[i-1][j]
                    summ += img[i+1][j]
                    summ += img[i][j-1]
                    summ += img[i][j+1]
                    summ += img[i-1][j-1]
                    summ += img[i-1][j+1]
                    summ += img[i+1][j-1]
                    summ += img[i+1][j+1]
                    k += 8
                
                else:
                    if i > 0:
                        summ += img[i-1][j]
                        k += 1
                    if i < len_rows-1:
                        summ += img[i+1][j]
                        k += 1
                    if j > 0:
                        summ += img[i][j-1]
                        k += 1
                    if j < len_cols-1:
                        summ += img[i][j+1]
                        k += 1
                    if i > 0 and j > 0:
                        summ += img[i-1][j-1]
                        k += 1
                    if i > 0 and j < len_cols-1:
                        summ += img[i-1][j+1]
                        k += 1
                    if i < len_rows-1 and j > 0:
                        summ += img[i+1][j-1]
                        k += 1
                    if i < len_rows-1 and j < len_cols-1:
                        summ += img[i+1][j+1]
                        k += 1

                smoothed_img[i][j] = summ // k

        return smoothed_img