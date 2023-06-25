# Repeat and Missing Number Array

def findNumbers(arr):
    arr.sort()
    minNo = min(arr)
    maxNo = max(arr)
    for i in range(minNo, maxNo):
        if i not in arr:
            B = i
        if arr.count(i) == 2:
            A = i
    return (A, B)

arr=[3, 1, 2, 5, 3]
print(findNumbers(arr))
            
    