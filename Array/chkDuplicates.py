# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def duplicates(arr):
    n = len(arr)-1
    for i in range(n):
        num = arr[i]
        arr[i] = -100
        if num in arr:
            return True
    return False

if __name__ == "__main__":
    try:
        arr = []
        print ("Enter the elements:\n")
        while True:
            arr.append(int(input()))
    except: 
        print(duplicates(arr))