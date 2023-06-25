# Time complexity should be O(log n)
# This is binary search method, but 0 is thrown as minimum idky
def minElement(arr):
    min, n = arr[0] = len(arr)
    start, end = 0, n-1
       
    while start<end:
        mid = (start+end)//2
        if arr[mid] < min:
            min = arr[mid]
        if arr[start] <= arr[mid]:
            if min>arr[start] and min < arr[mid]:
                end = mid -1
            else:
                start = mid +1
        else:
            if min>arr[mid] and min<arr[end]:
                start = mid +1 
            else:
                end = mid -1
    return min

arr = [3,4,5,1,2]
print(minElement(arr))

# Best solution:
def findMin(nums):
    low=0
    high=len(nums)-1
    res=nums[0]
    while low<=high:
        if nums[low]<nums[high]:
            res=min(res,nums[low])
            break
        mid=(low+high)//2
        res=min(res,nums[mid])
        if nums[mid]>=nums[low]:
            low=mid+1
        else:
            high=mid-1
    return res