def rotate(arr):
    row, col = len(arr), len(arr[0])
    matrix = []
    for j in range(col):
        vector = []
        i = row-1
        while i >=0:
            vector.append(arr[i][j])
            i-=1
        matrix.append(vector)
       
    return matrix

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(arr))

    