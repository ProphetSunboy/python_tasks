def flood(image, val, i, j, color):
    """
    Recursive function to change the color of image[i][j] and
    connected pixels with the same val.
    """
    image[i][j] = color
    if i > 0 and image[i-1][j] == val:
        flood(image, val, i-1, j, color)
    if i < len(image)-1 and image[i+1][j] == val:
        flood(image, val, i+1, j, color)
    if j > 0 and image[i][j-1] == val:
        flood(image, val, i, j-1, color)
    if j < len(image[0])-1 and image[i][j+1] == val:
        flood(image, val, i, j+1, color)
        
def floodFill(image, sr: int, sc: int, color: int):
    """
    An image is represented by an m x n integer grid image where image[i][j]
    represents the pixel value of the image.

    You are also given three integers sr, sc, and color. You should perform a
    flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, plus any pixels
    connected 4-directionally to the starting pixel of the same color as the
    starting pixel, plus any pixels connected 4-directionally to those pixels
    (also with the same color), and so on.
    Replace the color of all of the aforementioned pixels with color.

    Return the modified image after performing the flood fill.
    """
    if color == image[sr][sc]:
        return image
    val = image[sr][sc]
    flood(image, val, sr, sc, color)
    return image

print(floodFill([[0,0,0],[0,0,0]], 0, 0, 0))