def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    
    for num in arr:
        count[num] = arr.count(num)
    
    for i in range(1, max_value + 1):
        count[i] += count[i - 1]
    
    output = [0] * len(arr)
    
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

arr = [1,4,1,2,7,5,2] 
print(counting_sort(arr))