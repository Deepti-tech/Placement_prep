import numpy as np

def zero(arr, row, col):
    arr1 = np.ones((row,col)) 
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                for l in range(col):
                    arr1[i][l] = 0
                for k in range(row):
                    arr1[k][j] = 0
            else:
                if arr1[i][j] == 0:
                    continue
                else:
                    arr1[i][j] = arr[i][j]
    return arr1

arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(zero(arr, 3, 4))       