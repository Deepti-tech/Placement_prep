# Product of Array Except Self
import numpy as np

def product(arr):
    n = len(arr)
    productArr = []
    for i in range(n):
        temp = arr[i]
        arr[i] = 1
        result = np.prod(arr)
        productArr.append(result)
        arr[i] = temp
    return productArr

arr = [1,2,3,4]
print(product(arr))
        
        