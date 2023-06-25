def rev(arr):
    n = len(arr)
    for i in range(0,n//2):
        t = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = t
    return arr
        

if __name__ == '__main__':
    try:
        arr = []
        while True:
            arr.append(int(input()))
    except:
        print(rev(arr))