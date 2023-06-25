def maxSubArray(nums):
    maxSum = nums[0]
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum

if __name__ == '__main__':
    try:
        arr = []
        while True:
            arr.append(int(input()))
    except:
        print(maxSubArray(arr))
