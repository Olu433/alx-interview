def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Initialize row with 1s
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Calculate inner values
        triangle.append(row)
    
    return triangle
