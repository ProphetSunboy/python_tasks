def land_perimeter(arr):
    """
    land_perimeter(arr)
        arr - list of strings.
        Function return total perimeter of all the islands.
        Each piece of land marked with 'X'
        while the water fields are represented as 'O'. 
        i.e. ['XOOXO',
              'XOOXO',
              'OOOXO',
              'XXOXO',
              'OXOOO'] 
        return "Total land perimeter: 24"
    """
    p = 0
    for i, row in enumerate(arr):
        for j, el in enumerate(row):
            if el == 'X':
                if i == 0 or arr[i-1][j] != 'X':
                    p += 1
                if j == 0 or arr[i][j-1] != 'X':
                    p += 1
                if j == len(row) - 1 or arr[i][j+1] != 'X':
                    p += 1
                if i == len(arr) - 1 or arr[i+1][j] != 'X':
                    p += 1
    return f'Total land perimeter: {p}'