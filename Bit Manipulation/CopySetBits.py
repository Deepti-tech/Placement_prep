def copySetBits(x, y, l, r):
    x = format(x, 'b')
    y = format(y, 'b')
    if len(x) > len(y):
        y = '0' * (len(x) - len(y)) + y
    else:
        x = '0' * (len(y)- len(x)) + x
    n = len(x)
    l, r = n-l, n-r
    x, y = list(x), list(y)
    if y[l] == '1':
        x[l] = '1'
    if y[r] == '1':
        x[r] = '1'
    ans = "".join(x)
    ans = int(ans, 2)
    return ans
        
print(copySetBits(x = 10, y = 13, l = 2, r = 3))
print(copySetBits(x = 8, y = 7, l = 1, r = 2))