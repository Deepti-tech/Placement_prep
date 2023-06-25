import random
def findkth(arr, k):
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    l, m, r = len(left), len(mid), len(right)
    if k <= l:
        return findkth(left, k)
    elif k > l+m:
        return findkth(right, k)
    else:
        return mid[0]
    
arr=[7, 10, 4, 3, 20, 15]
print(findkth(arr, 3))