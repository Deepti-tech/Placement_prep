# Time complexity should be O(n)
import random
def findKthLargest(nums, k):
    if not nums: return
    pivot = random.choice(nums)
    left =  [x for x in nums if x > pivot]
    mid  =  [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]
    
    L, M = len(left), len(mid)
    
    if k <= L:
        return findKthLargest(left, k)
    elif k > L + M:
        return findKthLargest(right, k - L - M)
    else:
        return mid[0]
    
arr=[3, 1, 2, 5, 3]
print(findKthLargest(arr, 1))