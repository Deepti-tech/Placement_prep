def uniqueNumbers(arr):
    uniqueVector = []
    for i in arr:
        if arr.count(i) != 2:
            uniqueVector.append(i)
    uniqueVector.sort()
    return uniqueVector

arr = [1, 2, 3, 2, 1, 4]
print(uniqueNumbers(arr))