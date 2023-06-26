def uniqueRow(row, matrix):
    res = []
    unique = set()
    
    for row in matrix:
        dec = int("".join(str(x) for x in row), 2)
        if dec not in unique:
            res.append(row)
        unique.add(dec)
        
    return res

row = 3
M = [[1, 1, 0, 1],[1, 0, 0, 1],[1, 1, 0, 1]]
print(uniqueRow(row, M))