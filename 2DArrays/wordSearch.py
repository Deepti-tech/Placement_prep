def wordSearch(arr, word):
    top, bottom, left, right = 0, 0, 0, 0
    row, col = len(arr), len(arr[0])
    k = 0
    flag = 0
    while k < len(word):
        for i in range(row):
            for j in range(col):
                if arr[i][j] == word[k]:
                    flag = 1
                else:
                    if arr[i-1][j] == word[k]:
                            top = i-1
                            while top >=0:
                                top-=1
                                if arr[i][j] == word[k]:
                                    flag = 1
        k+=1