# Given an integer array nums, find a subarray
#  that has the largest product, and return the product.

def largestProductValue(arr):
    currentProd = arr[0]
    maxProd = arr[0]
    
    for i in range(1,len(arr)):
        currentProd *= arr[i]
        maxProd = max(maxProd, currentProd)
        
        if currentProd < 0:
            currentProd = 1
    return maxProd

arr=[2,3,-2,4]
print(largestProductValue(arr))