# Find if there is a pair with a given sum in the rotated sorted Array
def pairExist(arr, sum):
    y = 0
    for x in arr:
        y = sum - x
        if y in arr:
            return True
    return False

arr = {11, 15, 6, 8, 9, 10}
print(pairExist(arr, 25))