# Given an array of integers nums, find the next permutation of nums.

def nxtPermutation(nums):
    n = len(nums)
    k, l = n - 2, n - 1
    while k >= 0 and nums[k] >= nums[k + 1]:
        k -= 1
    if k < 0:
        nums.reverse()
    else:
        while l > k and nums[l] <= nums[k]:
            l -= 1
        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1:n] = reversed(nums[k + 1:n])
    return nums

if __name__ == "__main__":
    arr = [1,2,3]
    print(nxtPermutation(arr))