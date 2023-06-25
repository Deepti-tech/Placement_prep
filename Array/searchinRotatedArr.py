# Search in Rotated Sorted Array

def search(nums, target):
    start, end = 0, len(nums) - 1
    mid = (start + end) // 2
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= target and nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[end] >= target and nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
    return -1

if __name__ == "__main__":
    target = 1
    arr = [4,5,6,7,8,0,1,2]
    print(search(arr,target))