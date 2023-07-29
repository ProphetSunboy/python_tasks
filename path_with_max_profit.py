def path_with_max_profit(prices: list[list[int]]):
    """
    Given the price matrix prices, return the max profit and it's path.

    Inside prices you can move right or down.

    :param list[list[int]] prices: matrix of prices
    :returns tuple (int max_profit, list path)

    Time complexity: O(n^2)
    Space complexity: O(2 * n^2)
    """
    matrix = [[0] * len(prices[0]) for _ in range(len(prices))]
    paths = [[0] * len(prices[0]) for _ in range(len(prices))]

    matrix[0][0] = 1
    for i in range(len(prices)):
        for j in range(len(prices[0])):
            matrix[i][j] = prices[i][j]

            if i > 0 and j > 0:
                matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])
                if matrix[i - 1][j] > matrix[i][j - 1]:
                    paths[i][j] = (i - 1, j)
                else:
                    paths[i][j] = (i, j - 1)
            elif i > 0:
                matrix[i][j] += matrix[i - 1][j]
                paths[i][j] = (i - 1, j)
            else:
                matrix[i][j] += matrix[i][j - 1]
                paths[i][j] = (i, j - 1)

    path = [(i, j)]
    while i > 0 or j > 0:
        path.append(paths[i][j])
        i, j = paths[i][j][0], paths[i][j][1]

    return (matrix[len(matrix) - 1][len(matrix[0]) - 1], path[::-1])


# print(path_with_max_profit([[0, 2, 2, 1], [3, 1, 1, 1], [4, 4, 2, 0]]))
