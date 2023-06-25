def commonStr(stringArr):
    common = []
    a = stringArr[0]
    b = stringArr[1]
    length = min(len(a), len(b))
    
    for j in range(length):
        if ord(a[j]) == ord(b[j]):
            common.append(a[j])
        else:
            break
        
    n = len(stringArr)
    length = len(common)
    
    for i in range(2,n):
        b = stringArr[i]
        for j in range(length):
            if ord(common[j]) == ord(b[j]):
                continue
            else:
                common.pop()
                break
    return common

arr = ["flower","floor","flight"]
print(commonStr(arr))

# Easy solution
# def longestCommonPrefix(self, v: List[str]) -> str:
#     ans=""
#     v=sorted(v)
#     first=v[0]
#     last=v[-1]
#     for i in range(min(len(first),len(last))):
#         if(first[i]!=last[i]):
#             return ans
#         ans+=first[i]
#     return ans 