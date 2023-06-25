def pairExist(arr):
    arr1 = arr
    finalList = []
    for z in arr:
        sum = -z
        del arr1[arr.index(z)]
        for x in arr1:
            y = sum - x
            del arr1[arr1.index(x)]
            if y in arr1:
                lst = []
                lst.append(z)
                lst.append(x)
                lst.append(y)
                finalList.append(lst)                
    return finalList

nums = [-1,0,1,2,-1,-4]
print(pairExist(nums))        
